from tkinter import *



boton = ""



    


def digito(num):



    global boton

    boton = boton + str(num)

    calculo.set(boton)


def convBinario2(num):


  if num==1:
    return 1
  elif num==0:
    return 0
  else:
    temp = "{0:b}".format(num)


    #calculo.set(vector2)
    return(temp)


def convHex(num):


  if num==1:
    return 1
  elif num==0:
    return 0
  else:
    temp = hex(num)


    #calculo.set(vector2)
    return(temp)

def igual():



    try:

        global boton

        total = str(eval(boton))

        calculo.set(total)

        boton = ""



    except:



        calculo.set(" error ")


def igual2():



    try:

        global boton
        total = str(eval(boton))

        x = convBinario2(int(total))


        total2 = str(x)
        #print(total2)
        #numint=int(total)
        #print (numint)
        calculo.set(total2)

        boton = ""

        



    except:



        calculo.set(" error ")


def igual3():



    try:

        global boton
        total = str(eval(boton))

        x = convHex(int(total))


        total2 = str(x)
        #print(total2)
        #numint=int(total)
        #print (numint)
        calculo.set(total2)

        boton = ""

        



    except:



        calculo.set(" error ")


def limpiar():

    calculo.set("")





if __name__ == "__main__":



    fondo = Tk()





    fondo.configure(background="blue")

    fondo.title("Calculadora")

    fondo.geometry("300x220")





    calculo = StringVar()

    datos = Entry(fondo, textvariable=calculo)

    datos.grid(columnspan=10, ipadx=50)









    tecla1 = Button(fondo, text=' 1 ', fg='white', bg='black',

                     command=lambda: digito(1), height=2, width=5)

    tecla1.grid(row=4, column=0)



    tecla2 = Button(fondo, text=' 2 ', fg='white', bg='black',

                     command=lambda: digito(2), height=2, width=5)

    tecla2.grid(row=4, column=1)



    tecla3 = Button(fondo, text=' 3 ', fg='white', bg='black',

                     command=lambda: digito(3), height=2, width=5)

    tecla3.grid(row=4, column=2)



    tecla4 = Button(fondo, text=' 4 ', fg='white', bg='black',

                     command=lambda: digito(4), height=2, width=5)

    tecla4.grid(row=3, column=0)



    tecla5 = Button(fondo, text=' 5 ', fg='white', bg='black',

                     command=lambda: digito(5), height=2, width=5)

    tecla5.grid(row=3, column=1)



    tecla6 = Button(fondo, text=' 6 ', fg='white', bg='black',

                     command=lambda: digito(6), height=2, width=5)

    tecla6.grid(row=3, column=2)



    tecla7 = Button(fondo, text=' 7 ', fg='white', bg='black',

                     command=lambda: digito(7), height=2, width=5)

    tecla7.grid(row=2, column=0)



    tecla8 = Button(fondo, text=' 8 ', fg='white', bg='black',

                     command=lambda: digito(8), height=2, width=5)

    tecla8.grid(row=2, column=1)



    tecla9 = Button(fondo, text=' 9 ', fg='white', bg='black',

                     command=lambda: digito(9), height=2, width=5)

    tecla9.grid(row=2, column=2)



    tecla0 = Button(fondo, text=' 0 ', fg='white', bg='black',

                     command=lambda: digito(0), height=2, width=5)

    tecla0.grid(row=5, column=0)



    suma = Button(fondo, text=' + ', fg='white', bg='black',

                  command=lambda: digito("+"), height=2, width=5)

    suma.grid(row=2, column=3)



    resta = Button(fondo, text=' - ', fg='white', bg='black',

                   command=lambda: digito("-"), height=2, width=5)

    resta.grid(row=3, column=3)



    multiplica = Button(fondo, text=' * ', fg='white', bg='black',

                      command=lambda: digito("*"), height=2, width=5)

    multiplica.grid(row=4, column=3)



    divide = Button(fondo, text=' / ', fg='white', bg='black',

                    command=lambda: digito("/"), height=2, width=5)

    divide.grid(row=5, column=3)



    resultado = Button(fondo, text=' = ', fg='white', bg='black',

                   command=igual, height=2, width=5)

    resultado.grid(row=5, column=2)



    limpiar = Button(fondo, text='C', fg='white', bg='black',

                   command=limpiar, height=2, width=5)

    limpiar.grid(row=5, column=1)

    binario = Button(fondo, text='Bi', fg='white',bg='black',

                     #numint=int(num)
                     command=igual2 ,height=2, width=5)
    
    binario.grid(row=5, column=4) 

    Hex = Button(fondo, text='Hex', fg='white',bg='black',

                     #numint=int(num)
                     command=igual3 ,height=2, width=5)
    
    Hex.grid(row=4, column=4) 

fondo.mainloop()    
