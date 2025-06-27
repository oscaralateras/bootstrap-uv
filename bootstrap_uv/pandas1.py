import click
import pandas as pd
import numpy as np
 

def get_numof_customers(df):
    """Get the number of unique customers from the DataFrame."""
    return len(df['Customer'].unique())

def get_postcodes(df):
    """Get the all of unique postcodes from the DataFrame."""
    return df['Postcode'].unique()

def get_top10(df):
    """Get the top 10 customers from the DataFrame."""
    energy_cols = df.columns[[0]].tolist() + df.columns[5:-1].tolist()
    id_col = energy_cols[0]
    energy_cols = energy_cols[1:]

    agg_df = df.groupby(id_col)[energy_cols].sum().reset_index()
    agg_df["total_average_consumption"] = agg_df[energy_cols].mean(axis=1)
    agg_df.sort_values(by="total_average_consumption", ascending=False, inplace=True)

    # Return list of (ID, average) tuples
    return list(agg_df[[id_col, "total_average_consumption"]].head(10).itertuples(index=False, name=None))


@click.command("pandas1", help="Convert array to pandas DataFrame")
@click.option("--file", required=True, type=click.Path(exists=True), help="Input file path")
@click.option("--mode", type=click.Choice(['cust', 'postcodes', 'top10']), required=True, help="Operation mode: cust (count customers), postcodes (count unique postcodes), top10 (show top 10 customers)")
def pandas1(file, mode):
    """Convert Array to DataFrame."""
    try:
        df = pd.read_csv(file, header = 1)
        
        if mode == 'cust':
            customers = get_numof_customers(df)
            click.echo(f"Customers: {customers}")
        elif mode == 'postcodes':
            postcodes = get_postcodes(df)    
            click.echo(f"Unique Postcodes: {postcodes}")
        elif mode == 'top10':
            top_customers = get_top10(df)
            click.echo("Top 10 Customers:")
            for cust in top_customers:
                click.echo(f"Customer ID {cust}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)
        raise
