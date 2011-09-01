import csv

import riak


def import_csv_google_data():
    # set up client
    client = riak.RiakClient(
        host="127.0.0.1", port=8087, transport_class=riak.RiakPbcTransport)
    # set up bucket
    bucket = client.bucket('google-stock-data')
    # read in CSV data
    reader = csv.DictReader(open("data/goog.csv", "rb"))
    # iterate through the rows and put them in the bucket
    count = 0
    for row in reader:
        print ".",
        stock_quote = bucket.new(row.get("Date"), data=row)
        try:
            stock_quote.store()
        except Exception, error:
            print "Error while attempting to insert row %s" % count
            raise error
        count += 1
    print "\nDONE. Imported %s rows into Riak." % count
