import surfaces as s
import classes as c
import global_variable as g
import gun_class as gn

car = c.Car(500, 342, 0,
            0, False, 2000,
            s.surface_of_car,
            s.width_of_images['car'],
            s.height_of_images['car']
            )
dude = c.Dude(550, 350, 0,
              0, 10 / g.FPS * 30,
              8, 1, 0, 1000,
              [0] * 10, 2000, car,
              s.surface_of_dude_left, 'hp',
              s.width_of_images['dude'],
              s.height_of_images['dude'],
              {'fact': False, 'time': 0}
              )
button_shop = [c.ButtonObjects(1100, 0, s.shop_button),
               c.ButtonObjects(1100, 0, s.shop_close_button)]
start_button = c.ButtonObjects(400, 350, s.start_window)
quit_button = c.ButtonObjects(400, 340, s.quit_window)

full_arsenal = [gn.Gun(s.surface_of_pistol,
                       speed=500, damage=2,
                       magaz=15, reload=2000,
                       amount=1, spread=2, long=45
                       ),
                gn.Gun(s.surface_of_revolver,
                       speed=1000, damage=5,
                       magaz=6, reload=3000,
                       amount=1, spread=1, long=45
                       ),
                gn.Gun(s.surface_of_shotgun,
                       speed=1000, damage=1,
                       magaz=2, reload=3000,
                       amount=10, spread=300, long=45
                       ),
                gn.Gun(s.surface_of_uzi,
                       speed=100, damage=1,
                       magaz=30, reload=3000,
                       amount=1, spread=5, long=45
                       ),
                gn.Gun(s.surface_of_rifle,
                       speed=1000, damage=5,
                       magaz=5, reload=3000,
                       amount=1, spread=2, long=45
                       )
                ]
