#!/usr/bin/env python
"""Execute the tests for stellar.

The golden test outputs are generated by the script generate_outputs.sh.

You have to give the root paths to the source and the binaries as arguments to
the program.  These are the paths to the directory that contains the 'projects'
directory.

Usage:  run_tests.py SOURCE_ROOT_PATH BINARY_ROOT_PATH
"""
import logging
import os
import os.path
import sys

# Automagically add util/py_lib to PYTHONPATH environment variable.
path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..',
                                    '..', '..', 'util', 'py_lib'))
sys.path.insert(0, path)

import seqan.app_tests as app_tests

def add_tests():
    pass

def main(source_base, binary_base):
    """Main entry point of the script."""

    print('Executing test for stellar')
    print('=========================')
    print()

    # stellar/tests directory
    app_test_dir=os.path.join(source_base, 'test/cli') # original: 'apps/stellar/tests'
    relative_binary_path="." # original: 'apps/stellar'

    ph = app_tests.TestPathHelper(
        source_base, binary_base,
        app_test_dir)  # tests dir

    # ============================================================
    # Auto-detect the binary path.
    # ============================================================

    path_to_program = app_tests.autolocateBinary(
      binary_base, relative_binary_path, 'stellar')

    # ============================================================
    # Built TestConf list.
    # ============================================================

    # Build list with TestConf objects, analoguely to how the output
    # was generated in generate_outputs.sh.
    conf_list = []

    # We prepare a list of transforms to apply to the output files.  This is
    # used to strip the input/output paths from the programs' output to
    # make it more canonical and host independent.
    ph.outFile('-')  # To ensure that the out path is set.
    transforms = [
        app_tests.ReplaceTransform(os.path.join(ph.source_base_path, app_test_dir) + os.sep, '', right=True),
        app_tests.ReplaceTransform(ph.temp_dir + os.sep, '', right=True),
        app_tests.NormalizeScientificExponentsTransform(),
        ]

    # ============================================================
    # Run STELLAR.
    # ============================================================

    shortFlags = {
        'forward': ['-f'],
        'reverse': ['-r'],
        'both': [],
        'dna': ['-a', 'dna'],
        'dna5': [] # in short flags we let dna5 be empty, since it the default value
    }
    longFlags = {
        'forward': ['--forward'],
        'reverse': ['--reverse'],
        'both': [],
        'dna': ['--alphabet', 'dna'],
        'dna5': ['--alphabet', 'dna5']
    }

    for alphabet in ['dna', 'dna5']:
        for databaseStrand in ['forward', 'reverse', 'both']:
            for outputExt in ['gff', 'txt']:

                tmpSubDir = "{alphabet}_{databaseStrand}/".format(alphabet = alphabet, databaseStrand = databaseStrand)
                expectDataDir = ph.inFile('gold_standard/%s' % tmpSubDir)

                # Error rate 0.1:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('e-1.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=shortFlags.get(alphabet, []) +
                         shortFlags.get(databaseStrand, []) +
                         ['-e', '0.1', # --epsilon
                          '-l', '50', # --minLength
                          '-x', '10', # --xDrop
                          '-k', '7', # --kmer
                          '-n', '5000', # --numMatches
                          '-s', '10000', # --sortThresh
                          '-v', # --verbose
                          '-t', # --no-rt # for stable output
                          '--out', ph.outFile('e-1.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_e-1.fa'),
                          ph.inFile('512_simSeq2_e-1.fa')],
                    to_diff=[(ph.inFile(expectDataDir + 'e-1.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('e-1.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + 'e-1.{ext}'.format(ext = outputExt)),
                              ph.outFile('e-1.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Error rate 0.05:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('5e-2.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.05',
                          '--minLength', '50',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('5e-2.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_5e-2.fa'),
                          ph.inFile('512_simSeq2_5e-2.fa')],
                    to_diff=[(ph.inFile(expectDataDir + '5e-2.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('5e-2.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + '5e-2.{ext}'.format(ext = outputExt)),
                              ph.outFile('5e-2.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Error rate 0.25:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('25e-3.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.025',
                          '--minLength', '50',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('25e-3.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_25e-3.fa'),
                          ph.inFile('512_simSeq2_25e-3.fa')],
                    to_diff=[(ph.inFile(expectDataDir + '25e-3.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('25e-3.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + '25e-3.{ext}'.format(ext = outputExt)),
                              ph.outFile('25e-3.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Error rate 0.75:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('75e-3.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.075',
                          '--minLength', '50',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('75e-3.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_75e-3.fa'),
                          ph.inFile('512_simSeq2_75e-3.fa')],
                    to_diff=[(ph.inFile(expectDataDir + '75e-3.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('75e-3.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + '75e-3.{ext}'.format(ext = outputExt)),
                              ph.outFile('75e-3.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Error rate 0.0001:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('e-4.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.0001',
                          '--minLength', '50',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('e-4.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_e-4.fa'),
                          ph.inFile('512_simSeq2_e-4.fa')],
                    to_diff=[(ph.inFile(expectDataDir + 'e-4.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('e-4.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + 'e-4.{ext}'.format(ext = outputExt)),
                              ph.outFile('e-4.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Minimal length: 20, Error rate 0.05:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('minLen20.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.05',
                          '--minLength', '20',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('minLen20.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_5e-2.fa'),
                          ph.inFile('512_simSeq2_5e-2.fa')],
                    to_diff=[(ph.inFile(expectDataDir + 'minLen20.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('minLen20.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + 'minLen20.{ext}'.format(ext = outputExt)),
                              ph.outFile('minLen20.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

                # Minimal length: 150, Error rate 0.05:
                conf = app_tests.TestConf(
                    program=path_to_program,
                    redir_stdout=ph.outFile('minLen150.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                    args=longFlags.get(alphabet, []) +
                         longFlags.get(databaseStrand, []) +
                         ['--epsilon', '0.05',
                          '--minLength', '150',
                          '--xDrop', '10',
                          '--kmer', '7',
                          '--numMatches', '5000',
                          '--sortThresh', '10000',
                          '--verbose',
                          '--no-rt', # for stable output
                          '--out', ph.outFile('minLen150.{ext}'.format(ext = outputExt), tmpSubDir),
                          ph.inFile('512_simSeq1_5e-2.fa'),
                          ph.inFile('512_simSeq2_5e-2.fa')],
                    to_diff=[(ph.inFile(expectDataDir + 'minLen150.{ext}.stdout'.format(ext = outputExt)),
                              ph.outFile('minLen150.{ext}.stdout'.format(ext = outputExt), tmpSubDir),
                              transforms),
                             (ph.inFile(expectDataDir + 'minLen150.{ext}'.format(ext = outputExt)),
                              ph.outFile('minLen150.{ext}'.format(ext = outputExt), tmpSubDir),
                              transforms)])
                conf_list.append(conf)

    # ============================================================
    # Execute the tests.
    # ============================================================
    failures = 0
    try:
        for conf in conf_list:
            print(' '.join([conf.program] + conf.args))
            res = app_tests.runTest(conf)
            # Output to the user.
            if res:
                 print('OK')
            else:
                failures += 1
                print('FAILED')
    except Exception as e:
        raise e # This exception is saved, then finally is executed, and then the exception is raised.
    finally:
        # Cleanup.
        ph.deleteTempDir()

    print('==============================')
    print('     total tests: %d' % len(conf_list))
    print('    failed tests: %d' % failures)
    print('successful tests: %d' % (len(conf_list) - failures))
    print('==============================')
    # Compute and return return code.
    return failures != 0


if __name__ == '__main__':
    sys.exit(app_tests.main(main))
