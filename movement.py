import tkinter as tk


window_width = 800
window_height = 600
root = tk.Tk()
canvas = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canvas.pack(side=tk.TOP)
character = []
x = 160
y = 110
character.append(canvas.create_oval((150, 100, 170, 120), fill='yellow'))
character.append(canvas.create_oval((155, 105, 165, 115), fill='red'))
vx = 0
vy = 0

print('Управление:' + '\n' + 'Стрелки отвечают за перемещение персонажа' + '\n' + 'Выстрел - клавиша пробел' + '\n' + 'Поменять направление стрельбы (с права на лево и наоборот) - клавиша Enter')



def on_key_press(event):
    global vx, vy
    if event.keysym == 'Left':
        vx = -5
    elif event.keysym == 'Right':
        vx = 5
    elif event.keysym == 'Up':
        vy = -5
    elif event.keysym == 'Down':
        vy = 5
    elif event.keysym == 'space':
        bullet.fire()
    elif event.keysym == 'Return':
        bullet.change_direction()


def on_key_release(event):
    global vx, vy
    if event.keysym in ('Left', 'Right'):
        vx = 0
    elif event.keysym in ('Up', 'Down'):
        vy = 0


class bullet():
  def __init__(self, bullet_x, bullet_y):
      """ Конструктор класса bullet
      Args:
      x(int) - начальное положение по горизонтали
      y(int) - начальное положение по вертикали
      r(int) - радиус
      v(int) - скорость по оси x
      """
      self.x = bullet_x
      self.y = bullet_y
      self.r = 5
      self.v = 15
      self.direction = 1
      self.c = 1
      self.id = canvas.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill='orange'
      )

  def change_direction(self):
    if self.direction == 1:
      self.c = 0
    else:
      self.c = 1
  
  def fire(self):
        """Выстрелить.
        """
        if self.x > 810 or self.x < -10:
          self.x = x
          self.y = y
          self.direction = self.c

  def bullet_move(self):
        """Переместить пулю по прошествии единицы времени.
        """
        if self.y != 900:
          if self.direction == 1:
            self.x += self.v
          else:
            self.x -= self.v
          canvas.coords(self.id, self.x -self.r, self.y - self.r , self.x + self.r, self.y + self.r)

bullet = bullet(900, 900)
root.bind('<Key>', on_key_press)
root.bind('<KeyRelease>', on_key_release)

def game_loop():
    for thing in character:
      canvas.move(thing, vx, vy)
    global x, y
    x += vx
    y += vy
    root.after(50, game_loop)
    bullet.bullet_move()


game_loop()

root.mainloop()