#!/usr/bin/env python
import gzip
import sys
import io
import collections as c
import itertools as it
import elbalang.elbalang.elbalang as interpret
# from .elbalang import elbalang as interpret
import time

def get_data_as_list(file_ptr, delim=None):
    data_list = []
    if delim is None:
        return [i.split() for i in file_ptr]
    else:
        _delim = delim[0]
        for row_ptr in file_ptr:
            split_row = row_ptr.split()
            row_iter = it.chain(*[i.split(_delim) for i in split_row])
            resplit_row = [token for token in row_iter if token is not '']
            data_list.append(resplit_row)
    return data_list
        

def _analyze_experiment(f):
    start = time.time()
    row_list = get_data_as_list(f)
    analyze_result = interpret.elbalang.elbalang_run(row_list)
    # analyze_result = interpret.elbalang_run(row_list)
    end = time.time()
    analyze_result.append('time')
    analyze_result.append(round(end-start,2))
    analyze_result.append('total_len')
    analyze_result.append(len(row_list))
    return analyze_result


def _proc_zip_file(dest_to_unzip, experiment_zip):
    with open(experiment_zip, 'r') as f:
        zf = zipfile.ZipFile(f)
        zf.extractall(dest_to_unzip)

    for root, dirs, files in os.walk(dest_to_unzip):
        for _file in files:
            fname = os.path.join(root, _file)
            with open(fname, 'r') as f:
                return _analyze_experiment(f)


def _proc_gzip_file(file_path):
    with gzip.open(file_path, 'rt', encoding='utf-8') as gz:
        return _analyze_experiment(gz)


def _proc_file(file_path):
    if file_path.endswith('gz'):
        return _proc_gzip_file(file_path)
    elif file_path.endswith('zip'):
        return _proc_zip_file(file_path)
    else:
        with open(file_path, 'r') as f:
            return _analyze_experiment(f)


def proc_line(_line):
    line_parts = _line.split()
    path_to_file = line_parts[-1]
    return path_to_file 


def agg_analyze_files(file_of_paths, base):
    '''
        :params
        input
    '''
    total = c.Counter()

    with open(file_of_paths,'rt') as _files:
        for _line in _files:
            _file_path = proc_line(_line)
            _file = base + _file_path[1:]
            try:
                analyze_result = _proc_file(_file)
            except Exception as e:
                print('Skipping file', _file)
            else:
                hash_result = tuple(analyze_result)
                total[hash_result] += 1

    return total


def analyze_one_file(file_path):
    '''
        :params
        input
    '''
    try:
        
        analyze_result = _proc_file(file_path)
    except Exception as e:
        print(str(e), file_path)
        return None
    else:
        result = []
        result.append(file_path)
        result.extend(analyze_result)
        return result


def analyze_files(file_of_paths, base, output_file):
    '''
        :params
        input
    '''
    first_line = True

    with open(output_file, 'w') as _outf:
        with open(file_of_paths,'rt') as _files:
            for _line in _files:
                _file_path = proc_line(_line)
                _file = base + _file_path[1:]
                result = analyze_one_file(_file)
                if result:
                    values = result[2::2]
                    values_string = str(_file_path) + '|' + '|'.join(map(str,values)) + '\n'
                    if not first_line:
                        _outf.write(values_string)
                    else:
                        labels = result[1::2]
                        label_string = 'file_name|' + '|'.join(labels) + '\n'
                        _outf.write(label_string)
                        _outf.write(values_string)
                        first_line = False


def output_agg_file(result, output_file):
    '''
        output format: notes_log_lines
    '''
    written_first_line = False
    with open(output_file, 'w') as _out:
        for entry in result:
            #firsts, seconds = zip(*zip(entry[0::2], entry[1::2]))          
            values = entry[1::2]
            formatted_string = str(values[0]) + '|' + str(values[1]) + '|' + str(values[2]) + '|' + str(values[3]) + '|' + str(values[4]) + '|' + str(result[entry]) + '\n'
            if written_first_line:
                _out.write(formatted_string)
            else:
                header = '|'.join(entry[0::2])
                header = header + '|' + 'num_samples\n'
                _out.write(header)
                _out.write(formatted_string)
                written_first_line = True
