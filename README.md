# BitBar AppStore Plugin
BitBar plugin to show info about your iOS app.

## Ranking
Shows your iOS app ranking.

![screenshot](https://cloud.githubusercontent.com/assets/966109/13680763/6354f3c0-e73d-11e5-8c57-eb90bd5a53af.png)

### Setup
```python
feed_settings = [
  {
  'RANKING_TYPE': RANKING_TYPE['Top Free Applications'], # See list in file
  'GENRE'       : GENRE['Games'],                        # See list in file
  'COUNTRY'     : 'jp',                                  # Country code (ISO 3166-1 alpha-2)
  'LIMIT'       : 200,                                   # 1~200
  'APP_ID'      : 0000000000                             # Your app id
  }
]
```
