from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def map(request):
    return render(request, 'map.html')


def vis_nyc(request):
    csv_data = pd.read_csv('static/data/nyc_season_stat.csv') 
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "hotel": "0.9",
        "private": "45.17",
        "entire": "51.47",
        "shared": "2.46",
        "price_category": "0-100|100-200|200-300|300-400",
        "entire_list": "6.42|24.17|11.04|3.73",
        "private_list": "39.49|8.86|0.94|0.25",
        "hotel_list": "0.11|0.46|0.13|0.12",
        "share_list": "2.27|0.24|0.05|0.02",
        "region_category": "r1|r2|r3|r4|r5|r6|r7|r8",
        "entire_region_list": "77|22|11|24|15|15|34|46",
        "private_region_list": "124|12|52|43|11|42|54|22",
        "hotel_region_list": "7|12|12|2|1|6|45|3",
        "share_region_list": "6|2|5|8|9|95|23|34",
        "region_price": "12|24|35|12|92|93|123|144",
        "city": "nyc"
    }

    return render(request, 'vis.html', data)


def vis_london(request):
    csv_data = pd.read_csv('static/data/london_season_stat.csv') 
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "hotel": "1.77",
        "private": "42.23",
        "entire": "55.25",
        "shared": "0.74",
        "price_category": "0-100|100-200|200-300|300-400",
        "entire_list": "17.51|25.78|7.36|2.72",
        "private_list": "41.70|2.31|0.34|0.13",
        "hotel_list": "0.52|0.62|0.19|0.08",
        "share_list": "0.68|0.04|0.01|0.01",
        "region_category": "r1|r2|r3|r4|r5|r6|r7|r8",
        "entire_region_list": "77|22|11|24|15|15|34|46",
        "private_region_list": "124|12|52|43|11|42|54|22",
        "hotel_region_list": "7|12|12|2|1|6|45|3",
        "share_region_list": "6|2|5|8|9|95|23|34",
        "region_price": "12|24|35|12|92|93|123|144",
        "city": "london"
    }

    return render(request, 'vis.html', data)


def vis_beijing(request):
    csv_data = pd.read_csv('static/data/nyc_season_stat.csv') 
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "hotel": "0.9",
        "private": "45.17",
        "entire": "51.47",
        "shared": "2.46",
        "price_category": "0-100|100-200|200-300|300-400",
        "entire_list": "6.42|24.17|11.04|3.73",
        "private_list": "39.49|8.86|0.94|0.25",
        "hotel_list": "0.11|0.46|0.13|0.12",
        "share_list": "2.27|0.24|0.05|0.02",
        "region_category": "r1|r2|r3|r4|r5|r6|r7|r8",
        "entire_region_list": "77|22|11|24|15|15|34|46",
        "private_region_list": "124|12|52|43|11|42|54|22",
        "hotel_region_list": "7|12|12|2|1|6|45|3",
        "share_region_list": "6|2|5|8|9|95|23|34",
        "region_price": "12|24|35|12|92|93|123|144",
        "city": "beijing"
    }

    return render(request, 'vis.html', data)


def vis_paris(request):
    csv_data = pd.read_csv('static/data/nyc_season_stat.csv') 
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "hotel": "0.9",
        "private": "45.17",
        "entire": "51.47",
        "shared": "2.46",
        "price_category": "0-100|100-200|200-300|300-400",
        "entire_list": "6.42|24.17|11.04|3.73",
        "private_list": "39.49|8.86|0.94|0.25",
        "hotel_list": "0.11|0.46|0.13|0.12",
        "share_list": "2.27|0.24|0.05|0.02",
        "region_category": "r1|r2|r3|r4|r5|r6|r7|r8",
        "entire_region_list": "77|22|11|24|15|15|34|46",
        "private_region_list": "124|12|52|43|11|42|54|22",
        "hotel_region_list": "7|12|12|2|1|6|45|3",
        "share_region_list": "6|2|5|8|9|95|23|34",
        "region_price": "12|24|35|12|92|93|123|144",
        "city": "paris"
    }

    return render(request, 'vis.html', data)


def vis_tokyo(request):
    csv_data = pd.read_csv('static/data/tokyo_season_stat.csv') 
    date = csv_data["Date"].map(lambda x:x[2:10])
    date_list = date.values.tolist()

    avg = csv_data["avg_price"].map(lambda x:str(x))
    avg_list = avg.values.tolist()

    median = csv_data["median_price"].map(lambda x:str(x))
    median_list = median.values.tolist()

    data = {
        "date_list": '|'.join(date_list),
        "avg_list": '|'.join(avg_list),
        "median_list": '|'.join(median_list),
        "hotel": "10.5",
        "private": "20.6",
        "entire": "64.7",
        "shared": "4.19",
        "price_category": "0-10000|10000-20000|20000-30000|30000-40000",
        "entire_list": "18.32|30.12|9.52|2.61",
        "private_list": "15.47|6.25|1.23|0.31",
        "hotel_list": "7.09|3.49|0.58|0.05",
        "share_list": "4.70|0.26|0.01|0.0",
        "region_category": "r1|r2|r3|r4|r5|r6|r7|r8",
        "entire_region_list": "77|22|11|24|15|15|34|46",
        "private_region_list": "124|12|52|43|11|42|54|22",
        "hotel_region_list": "7|12|12|2|1|6|45|3",
        "share_region_list": "6|2|5|8|9|95|23|34",
        "region_price": "12|24|35|12|92|93|123|144",
        "city": "tokyo"
    }

    return render(request, 'vis.html', data)

