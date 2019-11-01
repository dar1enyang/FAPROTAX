# -*- coding: utf-8 -*-
#BEGIN_HEADER
import logging
import os

from installed_clients.KBaseReportClient import KBaseReport
import subprocess
#END_HEADER


class yangdar1en_FAPROTAX:
    '''
    Module Name:
    yangdar1en_FAPROTAX

    Module Description:
    A KBase module: yangdar1en_FAPROTAX
    '''

    ######## WARNING FOR GEVENT USERS ####### noqa
    # Since asynchronous IO can lead to methods - even the same method -
    # interrupting each other, you must be *very* careful when using global
    # state. A method could easily clobber the state set by another while
    # the latter method is running.
    ######################################### noqa
    VERSION = "0.0.1"
    GIT_URL = ""
    GIT_COMMIT_HASH = ""

    #BEGIN_CLASS_HEADER
    #END_CLASS_HEADER

    # config contains contents of config file in a hash or None if it couldn't
    # be found
    def __init__(self, config):
        #BEGIN_CONSTRUCTOR
        self.callback_url = os.environ['SDK_CALLBACK_URL']
        self.shared_folder = config['scratch']
        logging.basicConfig(format='%(created)s %(levelname)s: %(message)s',
                            level=logging.INFO)
        #END_CONSTRUCTOR
        pass

    def run_yangdar1en_FAPROTAX(self, ctx, params):
        """
        This example function accepts any number of parameters and returns results in a KBaseReport
        :param params: instance of mapping from String to unspecified object
        :returns: instance of type "ReportResults" -> structure: parameter
           "report_name" of String, parameter "report_ref" of String
        """
        # ctx is the context object
        # return variables are: output
        #BEGIN run_yangdar1en_FAPROTAX

        # subprocess.call(
        #     ["python", "../installed_clients/FAPROTAX/collapse_table.py"] + params, shell=False)
        result = True

        try:

            # subprocess.check_call(['python', '../installed_clients/FAPROTAX/collapse_table.py', '-i', '../installed_clients/FAPROTAX/phyloseq_test.biom',
            #                        '-o', '../installed_clients/FAPROTAX/test_result.biom', '-g', '../installed_clients/FAPROTAX/FAPROTAX.txt', '-v'], shell=True)
            resp = subprocess.check_call(['python', '../installed_clients/FAPROTAX/collapse_table.py', '-i', '../installed_clients/FAPROTAX/phyloseq_test.biom',
                                          '-o', self.shared_folder + '/test_result.biom', '-g', '../installed_clients/FAPROTAX/FAPROTAX.txt', '-v'], shell=True)
            print("No is: %d" % resp)
            if resp != 200:
                raise RuntimeError("didn't work good")
            # subprocess.check_call("exit 1", shell=True)
        except subprocess.CalledProcessError as error:
            result = False

        output = {'result': result}

        #END run_yangdar1en_FAPROTAX

        # At some point might do deeper type checking...
        if not isinstance(output, dict):
            raise ValueError('Method run_yangdar1en_FAPROTAX return value ' +
                             'output is not type dict as required.')
        # return the results
        return [output]

    def status(self, ctx):
        #BEGIN_STATUS
        returnVal = {'state': "OK",
                     'message': "",
                     'version': self.VERSION,
                     'git_url': self.GIT_URL,
                     'git_commit_hash': self.GIT_COMMIT_HASH}
        #END_STATUS
        return [returnVal]
