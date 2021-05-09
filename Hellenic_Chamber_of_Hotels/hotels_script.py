# API_ADDRESS: https://www.grhotels.gr/wp-admin/admin-ajax.php
# Fields:
# s_regions: Perifereia

# Headers
# accept: */*
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# content-length: 2075
# content-type: application/x-www-form-urlencoded; charset=UTF-8
# cookie: _ga=GA1.2.227392196.1592560779; _gid=GA1.2.938243019.1592560779; wp-wpml_current_language=el
# origin: https://www.grhotels.gr
# referer: https://www.grhotels.gr/touristikos-odigos/anazitisi-ksenodocheion-kai-kampingk?s_listing_type[]=293&s_regions=311&location_term_id=311
# sec-fetch-dest: empty
# sec-fetch-mode: cors
# sec-fetch-site: same-origin
# user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36

# Body
# action: wiloke_loadmore_listing_layout
# posts_per_page: 10
# listing_locations: 311
# listing_locations_region: 311
# listing_locations_regional_unit:
# listing_locations_municipality:
# latLng:
# listing_types[]: 293
# listing_islands:
# get_posts_from:
# is_focus_query: true
# is_open_now: false
# is_highest_rated: false
# paged: 1
# customerUTCTimezone: UTC+3
# s:
# displayStyle: loadmore
# atts[layout]: listing--list
# atts[get_posts_from]: the_both_listing_location_and_listing_cat
# atts[listing_cat]:
# atts[listing_location]:
# atts[listing_tag]:
# atts[include]:
# atts[show_terms]: both
# atts[filter_type]: none
# atts[btn_name]: Δείτε Περισσότερα
# atts[viewmore_page_link]: #
# atts[btn_position]: text-center
# atts[order_by]: title
# atts[order]: ASC
# atts[display_style]: loadmore
# atts[btn_style]: listgo-btn--default
# atts[btn_size]: listgo-btn--small
# atts[posts_per_page]: 10
# atts[image_size]: medium
# atts[toggle_render_favorite]: enable
# atts[favorite_description]: Save
# atts[toggle_render_view_detail]: enable
# atts[view_detail_text]:
# atts[toggle_render_find_direction]: enable
# atts[find_direction_text]:
# atts[toggle_render_link_to_map_page]: enable
# atts[link_to_map_page_text]:
# atts[toggle_render_post_excerpt]: enable
# atts[toggle_render_address]: enable
# atts[toggle_render_author]: enable
# atts[toggle_render_rating]: enable
# atts[limit_character]: 100
# atts[filter_result_description]: *open_result* %found_listing% %result_text=Result|Results% *end_result* in %total_listing% Destinations
# atts[block_id]:
# atts[css]:
# atts[map_page]:
# atts[term_ids]:
# atts[post_authors]:
# atts[created_at]:
# atts[extract_class]:
# atts[location_latitude_longitude]:
# atts[s_within_radius]: 10
# atts[s_unit]: km
# atts[isTax]: false
# atts[sidebar]: right
# atts[wrapper_class]: listings listings--list
# atts[item_class]: listing listing--list
# atts[before_item_class]: col-xs-12
# currentPageID: 384

# Ιστοσελίδα: www.hotelathanasia.gr
# E-Mail: athanasiahotel@yahoo.com
# Τηλέφωνο: 25930-22545
# Τηλέφωνο 2: 6948573638
# Εναλλακτικό Τηλέφωνο: 6948573638
# Πόλη: Θάσος
# Διεύθυνση: ΛΙΜΕΝΑΣ ΘΑΣΟΥ
# Ταχυδρομικός Κώδικας: 640 04

from bs4 import BeautifulSoup
import requests
import urllib.parse
import json
import csv

body = {
    'action':'wiloke_loadmore_listing_layout',
    'posts_per_page':'5000',
    'listing_locations':'270',
    'listing_locations_region':'270',
    'listing_locations_regional_unit':'',
    'listing_locations_municipality':'',
    'latLng':'',
    'listing_types[]':'293',
    'listing_islands':'',
    'get_posts_from':'',
    'is_focus_query':'true',
    'is_open_now':'false',
    'is_highest_rated':'false',
    'paged':'1',
    'customerUTCTimezone':'UTC+3',
    's':'',
    'displayStyle':'loadmore',
    'atts[layout]':'listing--list',
    'atts[get_posts_from]':'the_both_listing_location_and_listing_cat',
    'atts[listing_cat]':'',
    'atts[listing_location]':'',
    'atts[listing_tag]':'',
    'atts[include]':'',
    'atts[show_terms]':'both',
    'atts[filter_type]':'none',
    'atts[btn_name]':'Δείτε+Περισσότερα',
    'atts[viewmore_page_link]':'#',
    'atts[btn_position]':'text-center',
    'atts[order_by]':'title',
    'atts[order]':'ASC',
    'atts[display_style]':'loadmore',
    'atts[btn_style]':'listgo-btn--default',
    'atts[btn_size]':'listgo-btn--small',
    'atts[posts_per_page]':'10',
    'atts[image_size]':'medium',
    'atts[toggle_render_favorite]':'enable',
    'atts[favorite_description]':'Save',
    'atts[toggle_render_view_detail]':'enable',
    'atts[view_detail_text]':'',
    'atts[toggle_render_find_direction]':'enable',
    'atts[find_direction_text]':'',
    'atts[toggle_render_link_to_map_page]':'enable',
    'atts[link_to_map_page_text]':'',
    'atts[toggle_render_post_excerpt]':'enable',
    'atts[toggle_render_address]':'enable',
    'atts[toggle_render_author]':'enable',
    'atts[toggle_render_rating]':'enable',
    'atts[limit_character]':'100',
    'atts[filter_result_description]':'*open_result*+%found_listing%+%result_text=Result|Results%+*end_result*+in+%total_listing%+Destinations',
    'atts[block_id]':'',
    'atts[css]':'',
    'atts[map_page]':'',
    'atts[term_ids]':'',
    'atts[post_authors]':'',
    'atts[created_at]':'',
    'atts[extract_class]':'',
    'atts[location_latitude_longitude]':'',
    'atts[s_within_radius]':'10',
    'atts[s_unit]':'km',
    'atts[isTax]':'false',
    'atts[sidebar]':'right',
    'atts[wrapper_class]':'listings+listings--list',
    'atts[item_class]':'listing+listing--list',
    'atts[before_item_class]':'col-xs-12',
    'currentPageID':'384'
}

headers = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'origin': 'https://www.grhotels.gr',
    'referer': 'https://www.grhotels.gr/touristikos-odigos/anazitisi-ksenodocheion-kai-kampingk?s_listing_type[]=293&s_regions=311&location_term_id=311',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest'
}

url = 'https://www.grhotels.gr/wp-admin/admin-ajax.php'
path = '/wp-admin/admin-ajax.php'

regions = {
       'Ανατολικής Μακεδονίας και Θράκης': 311,
       'Αττικής': 270,
       'Βορείου Αιγαίου': 366,
       'Δυτικής Ελλάδας': 342,
       'Δυτικής Μακεδονίας': 334,
       'Ηπείρου': 347,
       'Θεσσαλίας': 328,
       'Ιονίων Νήσων': 319,
       'Κεντρικής Μακεδονίας': 322,
       'Κρήτης': 351,
       'Νοτίου Αιγαίου': 315,
       'Πελοποννήσου': 331,
       'Στερεάς Ελλάδας': 301
}
for region in regions:
    body['listing_locations'] = regions[region]
    body['listing_locations_region'] = regions[region]
    r = requests.post(url, data=body, headers=headers)
    json_object = json.loads(r.text)
    html = json_object['data']['content']
    soup = BeautifulSoup(html, "html.parser")

    columns = {"Όνομα": 1, "Απόσταση από νοσοκομείο": 2, "Αστέρια": 3}
    rows = []

    def add_unique(element, columns):
        if element not in columns.keys():
            columns[element] = len(columns.keys()) + 1


    star_classes = soup.select("div[class^=starTerm]")
    for star_class in star_classes:
        title = star_class.select("h3[class=listing__title]")
        uls = star_class.select("div.listgo__content ul.list-unstyled")
        distance = star_class.select(".grhotels-distance-icon-hospital")
        stars = star_class.select(".rating__star .fa-star")
        for ul in uls:
            lis = ul.find_all("li")
            row = {'Όνομα': title[0].text.strip(),
                   'Απόσταση από νοσοκομείο': distance[0].parent.text if distance is not None and len(distance) > 0 else '',
                   'Αστέρια': len(stars)}
            for li in lis:
                splits = li.text.split(": ")
                column_name = splits[0].strip()
                value = splits[1].strip()
                add_unique(column_name, columns)
                row[column_name] = value
            rows.append(row)

    print(len(rows), region)
    with open(region + '.csv', 'w', newline='') as csvfile:
        fieldnames = columns.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for row in rows:
            writer.writerow(row)
