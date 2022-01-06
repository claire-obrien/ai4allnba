#!/usr/bin/sh
# example: get_season_data.sh
#change the Season= numbers in the URL?
# redirect the output to a file (season_X_Y.json)
curl -v 'https://stats.nba.com/stats/leaguegamelog?Counter=1000&DateFrom=&DateTo=&Direction=DESC&LeagueID=00&PlayerOrTeam=P&Season=2021-22&SeasonType=Regular+Season&Sorter=DATE' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:95.0) Gecko/20100101 Firefox/95.0' -H 'Accept: application/json, text/plain, */*' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate, br' -H 'x-nba-stats-origin: stats' -H 'x-nba-stats-token: true' -H 'Origin: https://www.nba.com' -H 'DNT: 1' -H 'Connection: keep-alive' \
-H 'Referer: https://www.nba.com/' 
