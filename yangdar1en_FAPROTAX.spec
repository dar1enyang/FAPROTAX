/*
A KBase module: yangdar1en_FAPROTAX
*/

module yangdar1en_FAPROTAX {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_yangdar1en_FAPROTAX(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;
    
};
