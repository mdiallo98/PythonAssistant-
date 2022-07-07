import wolframalpha

app_id = '7PU8K2-TYL4XK4G5W'
client = wolframalpha.Client(app_id)

res = client.query('temperature in new york city today')

print(next(res.results).text)
