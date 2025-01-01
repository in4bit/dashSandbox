from dash import Dash, html, Input, Output

# Initialize the Dash app
app = Dash(__name__)

# Create a 10x10 grid layout
def create_grid():
    grid = []
    for row in range(10):
        row_elements = []
        for col in range(10):
            cell_id = f"cell-{row}-{col}"
            row_elements.append(
                html.Div(
                    id=cell_id,
                    style={
                        'width': '40px',
                        'height': '40px',
                        'backgroundColor': 'black',
                        'display': 'inline-block',
                        'margin': '2px',
                    },
                )
            )
        grid.append(html.Div(row_elements, style={'textAlign': 'center'}))
    return grid

# App layout
app.layout = html.Div(
    children=create_grid(),
    style={'display': 'flex', 'flexDirection': 'column', 'alignItems': 'center', 'marginTop': '50px'}
)

# Define callbacks to toggle cell colors
for row in range(10):
    for col in range(10):
        cell_id = f"cell-{row}-{col}"

        @app.callback(
            Output(cell_id, 'style'),
            Input(cell_id, 'n_clicks'),
            prevent_initial_call=True
        )
        def toggle_color(n_clicks, cell_id=cell_id):
            color = 'blue' if n_clicks and n_clicks % 2 else 'black'
            return {
                'width': '40px',
                'height': '40px',
                'backgroundColor': color,
                'display': 'inline-block',
                'margin': '2px',
            }

# Expose the WSGI server
server = app.server

if __name__ == "__main__":
    app.run_server(debug=True, host='0.0.0.0', port=8080)
