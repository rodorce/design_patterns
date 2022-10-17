from patterns import ReportFactory, csv_utils
from patterns.report_facade import ReportFacade
CSV_FILE = "taxi-data.csv"


def main():
    rides = csv_utils.parse_file(CSV_FILE)
    print_report = ReportFactory.get_report("print", rides)
    web_report = ReportFactory.get_report("web", rides)
    ReportFacade().generateReports(web_report, print_report)
    
if __name__ == '__main__':
    main()
