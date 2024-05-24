import tkinter as tk

root = tk.Tk()

# Carregue a imagem
image = tk.PhotoImage(file="gmail.png")

# Crie um botão com a imagem
button = tk.Button(master=root, text="Botão", image=image, compound=tk.LEFT)
# Você pode ajustar a posição da imagem alterando o valor de 'compound'

button.pack()
root.mainloop()