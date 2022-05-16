import tests
import pandas as pd
import dash
from dash import dcc
from dash import html
import plotly.graph_objects as go


pd.options.plotting.backend = "plotly"

# testing prefixTree
#tests.basic_test()

data = {"number_of_chars": [], "average_time_prefixTree": [], "average_time_prefixTree2": []}
for number_of_chars in range(3, 100):
    average_time, _ = tests.testing_times_of_inserting_random_strings(number_of_chars=number_of_chars)
    average_time2, _ = tests.testing_times_of_inserting_random_strings2(number_of_chars=number_of_chars)
    data["number_of_chars"].append(number_of_chars)
    data["average_time_prefixTree"].append(average_time)
    data["average_time_prefixTree2"].append(average_time2)
    print("number of chars: " + str(number_of_chars) + ". average time1: " + str(average_time) + ". average time2: " + str(average_time2))



# plotting number_of_chars with average time
df = pd.DataFrame(data)
fig = go.Figure()
fig = fig.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_prefixTree"],
                                 name="prefixTree"))
fig = fig.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_prefixTree2"],
                                 name="prefixTree2"))

data = {"number_of_chars": [], "average_time_find": [], "average_time_not_find": [], "average_time_find2": [], "average_time_not_find2": []}
for number_of_chars in range(3, 100):
    average_time_finding, average_time_not_finding = tests.testing_times_of_contains_random_strings(N=1000, number_of_chars=number_of_chars)
    average_time_finding2, average_time_not_finding2 = tests.testing_times_of_contains_random_strings2(N=1000, number_of_chars=number_of_chars)
    data["number_of_chars"].append(number_of_chars)
    data["average_time_find"].append(average_time_finding)
    data["average_time_not_find"].append(average_time_not_finding)
    data["average_time_find2"].append(average_time_finding2)
    data["average_time_not_find2"].append(average_time_not_finding2)
    print("number of chars: " + str(number_of_chars) + ". average time found: " + str(average_time_finding) + ". average time not found: " + str(average_time_not_finding))


# plotting number_of_chars with average time to find
df = pd.DataFrame(data)
fig2 = go.Figure()
fig2 = fig2.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_find"],
                                 name="str in PrefixTree"))
fig2 = fig2.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_not_find"],
                                 name="str not in PrefixTree"))
fig2 = fig2.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_find2"],
                                 name="str in PrefixTree2"))
fig2 = fig2.add_trace(go.Scatter(x=df["number_of_chars"],
                                 y=df["average_time_not_find2"],
                                 name="str not in PrefixTree2"))

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig),
    dcc.Graph(figure=fig2)
])

app.run_server(debug=True, use_reloader=False)

