import arcade

arcade.open_window(800, 800, "Pumpkin Face")
arcade.set_background_color(arcade.color.BLACK)
arcade.start_render()

arcade.draw_circle_filled(400, 400, 300, arcade.color.PUMPKIN)
arcade.draw_arc_outline(400, 300, 400, 100, arcade.color.BRUNSWICK_GREEN, -180, 0, 8)
arcade.draw_arc_filled(300, 450, 100, 200, arcade.color.BLACK, 0, 180)
arcade.draw_xywh_rectangle_filled(450, 450, 100, 100, arcade.color.BLACK)
arcade.draw_circle_filled(300, 490, 20, arcade.color.ELECTRIC_YELLOW)
arcade.draw_circle_filled(500, 490, 20, arcade.color.ELECTRIC_YELLOW)
arcade.draw_lrtb_rectangle_filled(150, 650, 750, 650, arcade.color.JAPANESE_CARMINE)
arcade.draw_triangle_filled(400, 400, 450, 300, 300, 300, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(300, 500, 800, 650, arcade.color.JAPANESE_CARMINE)
arcade.finish_render()
arcade.run()


