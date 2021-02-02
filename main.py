# main.py

# default single paper thickness 
t_0 = 0.00008

def app():
    """This function calculate the thickness of a paper
    and return the calculated value

    :thickness : the return value
    """

    # calculation
    thickness = t_0 * pow(2, 43)
    
    print('Thickness of sheet folded is: {}'.format(thickness))
    return thickness

if __name__ == "__main__":
    app()
    