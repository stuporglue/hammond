def set_alpha(color,alpha):

    alpha = min(alpha,1)
    alpha = max(alpha,0)

    color.red   = round(min(255,max(0,color.red * alpha)))
    color.green = round(min(255,max(0,color.green * alpha)))
    color.blue  = round(min(255,max(0,color.blue * alpha)))
    return color

def set_alphas(colors,alpha):
    for color in colors:
        color = set_alpha(color,alpha)

    return colors

def colorstr(color,pad=0):
    return str(color.red).zfill(pad) + "," + str(color.green).zfill(pad) + "," + str(color.blue).zfill(pad)
