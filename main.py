@namespace
class SpriteKind:
    Environment = SpriteKind.create()

def on_up_pressed():
    global up, down, left, right
    up = True
    down = False
    left = False
    right = False
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        . c d f d d f d e e d d f . . .
                        c d e e d d d d e e b d c . . .
                        c d d d d c d d e e b d c . f f
                        c c c c c d d d e e f c . f e f
                        . f d d d d d e e f f . . f e f
                        . . f f f f f e e e e f . f e f
                        . . . . f e e e e e e e f f e f
                        . . . f e f f e f e e e e f f .
                        . . . f e f f e f e e e e f . .
                        . . . f d b f d b f f e f . . .
                        . . . f d d c d d b b d f . . .
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        c d e e d d d d e e d d f . . .
                        c d d d d c d d e e b d c . . .
                        c c c c c d d e e e b d c . f f
                        . f d d d d e e e f f c . f e f
                        . f f f f f f e e e e f . f e f
                        . f f f f e e e e e e e f f e f
                        f d d f d d f e f e e e e f f .
                        f d b f d b f e f e e e e f . .
                        f f f f f f f f f f f f e f . .
                        . . . . . . . . . f c d d f . .
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f f . . . .
                        . c d d d d d d e e d d f . . .
                        . c d f d d f d e e b d c . . .
                        c d d f d d f d e e b d c . f f
                        c d e e d d d d e e f c . f e f
                        c d d d d c d e e e f . . f e f
                        . f c c c d e e e f f . . f e f
                        . . f f f f f e e e e f . f e f
                        . . . . f e e e e e e e f f f .
                        . . f f e f e e f e e e e f . .
                        . f e f f e e f f f e e e f . .
                        f d d b d d c f f f f f f b f .
                        f d d c d d d f . . f c d d f .
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f f f . . . .
                        . . f d d d e e e e d d f . . .
                        . c d d d d d e e e b d c . . .
                        . c d d d d d d e e b d c . . .
                        c d d f d d f d e e f c . f f .
                        c d d f d d f d e e f . . f e f
                        c d e e d d d d e e f . . f e f
                        . f d d d c d e e f f . . f e f
                        . . f f f d e e e e e f . f e f
                        . . . . f e e e e e e e f f f .
                        . . . . f f e e e e e b f f . .
                        . . . f e f f e e c d d f f . .
                        . . f d d b d d c f f f . . . .
                        . . f d d c d d d f f . . . . .
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        . c d f d d f d e e d d f . . .
                        c d e e d d d d e e b d c . . .
                        c d d d d c d d e e b d c . . .
                        c c c c c d d e e e f c . . . .
                        . f d d d d e e e f f . . . . .
                        . . f f f f f e e e e f . . . .
                        . . . . f f e e e e e e f . f f
                        . . . f e e f e e f e e f . e f
                        . . f e e f e e f e e e f . e f
                        . f b d f d b f b b f e f f e f
                        . f d d f d d f d d b e f f f f
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        True)
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_a_pressed():
    global projectile
    if up == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . 4 4 . . . . . . .
                            . . . . . . 4 5 5 4 . . . . . .
                            . . . . . . 2 5 5 2 . . . . . .
                            . . . . . . . 2 2 . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -1,
            -100)
    if down == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . 4 4 . . . . . . .
                            . . . . . . 4 5 5 4 . . . . . .
                            . . . . . . 2 5 5 2 . . . . . .
                            . . . . . . . 2 2 . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            1,
            50)
    if left == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . 4 4 . . . . . . .
                            . . . . . . 4 5 5 4 . . . . . .
                            . . . . . . 2 5 5 2 . . . . . .
                            . . . . . . . 2 2 . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            -100,
            -1)
    if right == True:
        projectile = sprites.create_projectile_from_sprite(img("""
                . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . 4 4 . . . . . . .
                            . . . . . . 4 5 5 4 . . . . . .
                            . . . . . . 2 5 5 2 . . . . . .
                            . . . . . . . 2 2 . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
                            . . . . . . . . . . . . . . . .
            """),
            mySprite,
            100,
            1)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_left_pressed():
    global left, down, right, up
    left = True
    down = False
    right = False
    up = False
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        . c d f d d f d e e d d f . . .
                        c d e e d d d d e e b d c . . .
                        c d d d d c d d e e b d c . f f
                        c c c c c d d d e e f c . f e f
                        . f d d d d d e e f f . . f e f
                        . . f f f f f e e e e f . f e f
                        . . . . f e e e e e e e f f e f
                        . . . f e f f e f e e e e f f .
                        . . . f e f f e f e e e e f . .
                        . . . f d b f d b f f e f . . .
                        . . . f d d c d d b b d f . . .
                        . . . . f f f f f f f f f . . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        c d e e d d d d e e d d f . . .
                        c d d d d c d d e e b d c . . .
                        c c c c c d d e e e b d c . f f
                        . f d d d d e e e f f c . f e f
                        . f f f f f f e e e e f . f e f
                        . f f f f e e e e e e e f f e f
                        f d d f d d f e f e e e e f f .
                        f d b f d b f e f e e e e f . .
                        f f f f f f f f f f f f e f . .
                        . . . . . . . . . f c d d f . .
                        . . . . . . . . . . f f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f f . . . .
                        . c d d d d d d e e d d f . . .
                        . c d f d d f d e e b d c . . .
                        c d d f d d f d e e b d c . f f
                        c d e e d d d d e e f c . f e f
                        c d d d d c d e e e f . . f e f
                        . f c c c d e e e f f . . f e f
                        . . f f f f f e e e e f . f e f
                        . . . . f e e e e e e e f f f .
                        . . f f e f e e f e e e e f . .
                        . f e f f e e f f f e e e f . .
                        f d d b d d c f f f f f f b f .
                        f d d c d d d f . . f c d d f .
                        . f f f f f f f . . . f f f . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f f f . . . .
                        . . f d d d e e e e d d f . . .
                        . c d d d d d e e e b d c . . .
                        . c d d d d d d e e b d c . . .
                        c d d f d d f d e e f c . f f .
                        c d d f d d f d e e f . . f e f
                        c d e e d d d d e e f . . f e f
                        . f d d d c d e e f f . . f e f
                        . . f f f d e e e e e f . f e f
                        . . . . f e e e e e e e f f f .
                        . . . . f f e e e e e b f f . .
                        . . . f e f f e e c d d f f . .
                        . . f d d b d d c f f f . . . .
                        . . f d d c d d d f f . . . . .
                        . . . f f f f f f f . . . . . .
            """),
            img("""
                . . . . f f f f f . . . . . . .
                        . . . f e e e e e f . . . . . .
                        . . f d d d d e e e f . . . . .
                        . c d f d d f d e e f f . . . .
                        . c d f d d f d e e d d f . . .
                        c d e e d d d d e e b d c . . .
                        c d d d d c d d e e b d c . . .
                        c c c c c d d e e e f c . . . .
                        . f d d d d e e e f f . . . . .
                        . . f f f f f e e e e f . . . .
                        . . . . f f e e e e e e f . f f
                        . . . f e e f e e f e e f . e f
                        . . f e e f e e f e e e f . e f
                        . f b d f d b f b b f e f f e f
                        . f d d f d d f d d b e f f f f
                        . . f f f f f f f f f f f f f .
            """)],
        100,
        True)
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_right_pressed():
    global right, left, up, down
    right = True
    left = False
    up = False
    down = False
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d f d d f d c .
                        . . . c d b e e d d d d e e d c
                        f f . c d b e e d d c d d d d c
                        f e f . c f e e d d d c c c c c
                        f e f . . f f e e d d d d d f .
                        f e f . f e e e e f f f f f . .
                        f e f f e e e e e e e f . . . .
                        . f f e e e e f e f f e f . . .
                        . . f e e e e f e f f e f . . .
                        . . . f e f f b d f b d f . . .
                        . . . f d b b d d c d d f . . .
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . . f e e d f d d f d c .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d d d d e e d c
                        . . . c d b e e d d c d d d d c
                        f f . c d b e e e d d c c c c c
                        f e f . c f f e e e d d d d f .
                        f e f . f e e e e f f f f f f .
                        f e f f e e e e e e e f f f f .
                        . f f e e e e f e f d d f d d f
                        . . f e e e e f e f b d f b d f
                        . . f e f f f f f f f f f f f f
                        . . f d d c f . . . . . . . . .
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . f f e e e d d d d f . .
                        . . . f d d e e d d d d d d c .
                        . . . c d b e e d f d d f d c .
                        f f . c d b e e d f d d f d d c
                        f e f . c f e e d d d d e e d c
                        f e f . . f e e e d c d d d d c
                        f e f . . f f e e e d c c c f .
                        f e f . f e e e e f f f f f . .
                        . f f f e e e e e e e f . . . .
                        . . f e e e e f e e f e f f . .
                        . . f e e e f f f e e f f e f .
                        . f b f f f f f f c d d b d d f
                        . f d d c f . . f d d d c d d f
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . f f f e e e e e f . . .
                        . . . f d d e e e e d d d f . .
                        . . . c d b e e e d d d d d c .
                        . . . c d b e e d d d d d d c .
                        . f f . c f e e d f d d f d d c
                        f e f . . f e e d f d d f d d c
                        f e f . . f e e d d d d e e d c
                        f e f . . f f e e d c d d d f .
                        f e f . f e e e e e d f f f . .
                        . f f f e e e e e e e f . . . .
                        . . f f b e e e e e f f . . . .
                        . . f f d d c e e f f e f . . .
                        . . . . f f f c d d b d d f . .
                        . . . . . f f d d d c d d f . .
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d f d d f d c .
                        . . . c d b e e d d d d e e d c
                        . . . c d b e e d d c d d d d c
                        . . . . c f e e e d d c c c c c
                        . . . . . f f e e e d d d d f .
                        . . . . f e e e e f f f f f . .
                        f f . f e e e e e e f f . . . .
                        f e . f e e f e e f e e f . . .
                        f e . f e e e f e e f e e f . .
                        f e f f e f b b f b d f d b f .
                        f f f f e b d d f d d f d d f .
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        True)
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_on_overlap(sprite, otherSprite):
    pause(1000)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.Environment, on_on_overlap)

def on_down_pressed():
    global down, up, left, right
    down = True
    up = False
    left = False
    right = False
    animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
    animation.run_image_animation(mySprite,
        [img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d f d d f d c .
                        . . . c d b e e d d d d e e d c
                        f f . c d b e e d d c d d d d c
                        f e f . c f e e d d d c c c c c
                        f e f . . f f e e d d d d d f .
                        f e f . f e e e e f f f f f . .
                        f e f f e e e e e e e f . . . .
                        . f f e e e e f e f f e f . . .
                        . . f e e e e f e f f e f . . .
                        . . . f e f f b d f b d f . . .
                        . . . f d b b d d c d d f . . .
                        . . . f f f f f f f f f . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . . f e e d f d d f d c .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d d d d e e d c
                        . . . c d b e e d d c d d d d c
                        f f . c d b e e e d d c c c c c
                        f e f . c f f e e e d d d d f .
                        f e f . f e e e e f f f f f f .
                        f e f f e e e e e e e f f f f .
                        . f f e e e e f e f d d f d d f
                        . . f e e e e f e f b d f b d f
                        . . f e f f f f f f f f f f f f
                        . . f d d c f . . . . . . . . .
                        . . f f f f . . . . . . . . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . f f e e e d d d d f . .
                        . . . f d d e e d d d d d d c .
                        . . . c d b e e d f d d f d c .
                        f f . c d b e e d f d d f d d c
                        f e f . c f e e d d d d e e d c
                        f e f . . f e e e d c d d d d c
                        f e f . . f f e e e d c c c f .
                        f e f . f e e e e f f f f f . .
                        . f f f e e e e e e e f . . . .
                        . . f e e e e f e e f e f f . .
                        . . f e e e f f f e e f f e f .
                        . f b f f f f f f c d d b d d f
                        . f d d c f . . f d d d c d d f
                        . . f f f . . . f f f f f f f .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . f f f e e e e e f . . .
                        . . . f d d e e e e d d d f . .
                        . . . c d b e e e d d d d d c .
                        . . . c d b e e d d d d d d c .
                        . f f . c f e e d f d d f d d c
                        f e f . . f e e d f d d f d d c
                        f e f . . f e e d d d d e e d c
                        f e f . . f f e e d c d d d f .
                        f e f . f e e e e e d f f f . .
                        . f f f e e e e e e e f . . . .
                        . . f f b e e e e e f f . . . .
                        . . f f d d c e e f f e f . . .
                        . . . . f f f c d d b d d f . .
                        . . . . . f f d d d c d d f . .
                        . . . . . . f f f f f f f . . .
            """),
            img("""
                . . . . . . . f f f f f . . . .
                        . . . . . . f e e e e e f . . .
                        . . . . . f e e e d d d d f . .
                        . . . . f f e e d f d d f d c .
                        . . . f d d e e d f d d f d c .
                        . . . c d b e e d d d d e e d c
                        . . . c d b e e d d c d d d d c
                        . . . . c f e e e d d c c c c c
                        . . . . . f f e e e d d d d f .
                        . . . . f e e e e f f f f f . .
                        f f . f e e e e e e f f . . . .
                        f e . f e e f e e f e e f . . .
                        f e . f e e e f e e f e e f . .
                        f e f f e f b b f b d f d b f .
                        f f f f e b d d f d d f d d f .
                        . f f f f f f f f f f f f f . .
            """)],
        100,
        True)
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_life_zero():
    sprites.destroy(mySprite2)
info.on_life_zero(on_life_zero)

def on_on_overlap2(sprite2, otherSprite2):
    sprites.destroy(mySprite3)
    sprites.destroy(projectile)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

moving = False
mySprite3: Sprite = None
projectile: Sprite = None
right = False
left = False
down = False
up = False
mySprite: Sprite = None
mySprite2: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level1
"""))
mySprite2 = sprites.create(img("""
        ....................e2e22e2e....................
            .................222eee22e2e222.................
            ..............222e22e2e22eee22e222..............
            ...........e22e22eeee2e22e2eeee22e22e...........
            ........eeee22e22e22e2e22e2e22e22e22eeee........
            .....222e22e22eeee22e2e22e2e22eeee22e22e222.....
            ...22eeee22e22e22e22eee22eee22e22e22e22eeee22...
            4cc22e22e22eeee22e22e2e22e2e22e22eeee22e22e22cc4
            6c6eee22e22e22e22e22e2e22e2e22e22e22e22e22eee6c6
            46622e22eeee22e22eeee2e22e2eeee22e22eeee22e22664
            46622e22e22e22eeee22e2e22e2e22eeee22e22e22e22664
            4cc22eeee22e22e22e22eee22eee22e22e22e22eeee22cc4
            6c622e22e22eeee22e22e2e22e2e22e22eeee22e22e226c6
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            46622e22eeee22e22e22e2e22e2e22e22e22eeee22e22664
            4cc22e22e22e22e22eeee2e22e2eeee22e22e22e22e22cc4
            6c622eeee22e22eeee22eee22eee22eeee22e22eeee226c6
            46622e22e22eeee22e22e2e22e2e22e22eeee22e22e22664
            466eee22e22e22e22e22e2e22e2e22e22e22e22e22eee664
            4cc22e22eeee22e22e22e2e22e2e22e22e22eeee22e22cc4
            6c622e22e22e22e22e22eee22eee22e22e22e22e22e226c6
            46622eeee22e22e22eeecc6666cceee22e22e22eeee22664
            46622e22e22e22eeecc6666666666cceee22e22e22e22664
            4cceee22e22eeecc66666cccccc66666cceee22e22eeecc4
            6c622e22eeecc66666cc64444446cc66666cceee22e226c6
            46622e22cc66666cc64444444444446cc66666cc22e22664
            46622cc6666ccc64444444444444444446ccc6666cc22664
            4ccc6666ccc6444bcc666666666666ccb4446ccc6666ccc4
            cccccccc6666666cb44444444444444bc6666666cccccccc
            64444444444446c444444444444444444c64444444444446
            66cb444444444cb411111111111111114bc444444444bc66
            666cccccccccccd166666666666666661dccccccccccc666
            6666444444444c116eeeeeeeeeeeeee611c4444444446666
            666e2222222e4c16e4e44e44e44e44ee61c4e2222222e666
            666eeeeeeeee4c16e4e44e44e44e44ee61c4eeeeeeeee666
            666eddddddde4c66f4e4effffffe44ee66c4eddddddde666
            666edffdffde4c66f4effffffffff4ee66c4edffdffde666
            666edccdccde4c66f4effffffffffeee66c4edccdccde666
            666eddddddde4c66f4eeeeeeeeeeeeee66c4eddddddde666
            c66edffdffde4c66e4e44e44e44e44ee66c4edffdffde66c
            c66edccdccde4c66e4e44e44e44e44ee66c4edccdccde66c
            cc66666666664c66e4e44e44e44feeee66c46666666666cc
            .c66444444444c66e4e44e44e44ffffe66c44444444466c.
            ..c64eee4eee4c66f4e44e44e44f44fe66c4eee4eee46c..
            ...c4eee4eee4c66f4e44e44e44effee66c4eee4eee4c...
            ....644444444c66f4e44e44e44e44ee66c444444446....
            .....64eee444c66f4e44e44e44e44ee66c444eee46.....
            ......6ccc666c66e4e44e44e44e44ee66c666ccc6......
    """),
    SpriteKind.Environment)
mySprite = sprites.create(img("""
        . . . . f f f f f . . . . . . .
            . . . f e e e e e f . . . . . .
            . . f d d d d e e e f . . . . .
            . c d f d d f d e e f f . . . .
            . c d f d d f d e e d d f . . .
            c d e e d d d d e e b d c . . .
            c d d d d c d d e e b d c . f f
            c c c c c d d d e e f c . f e f
            . f d d d d d e e f f . . f e f
            . . f f f f f e e e e f . f e f
            . . . . f e e e e e e e f f e f
            . . . f e f f e f e e e e f f .
            . . . f e f f e f e e e e f . .
            . . . f d b f d b f f e f . . .
            . . . f d d c d d b b d f . . .
            . . . . f f f f f f f f f . . .
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
info.set_score(0)
info.set_life(3)
mySprite.set_stay_in_screen(True)

def on_on_update():
    global moving
    moving = controller.left.is_pressed() or (controller.right.is_pressed() or (controller.up.is_pressed() or controller.down.is_pressed()))
    if not (moving):
        animation.stop_animation(animation.AnimationTypes.ALL, mySprite)
game.on_update(on_on_update)

def on_update_interval():
    global mySprite3
    mySprite3 = sprites.create(img("""
            . . . . c c c c c c . . . . . .
                    . . . c 6 7 7 7 7 6 c . . . . .
                    . . c 7 7 7 7 7 7 7 7 c . . . .
                    . c 6 7 7 7 7 7 7 7 7 6 c . . .
                    . c 7 c 6 6 6 6 c 7 7 7 c . . .
                    . f 7 6 f 6 6 f 6 7 7 7 f . . .
                    . f 7 7 7 7 7 7 7 7 7 7 f . . .
                    . . f 7 7 7 7 6 c 7 7 6 f c . .
                    . . . f c c c c 7 7 6 f 7 7 c .
                    . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                    . c 7 7 2 7 7 c f c 6 7 7 6 c c
                    c 1 1 1 1 7 6 f c c 6 6 6 c . .
                    f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                    f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                    . f 6 1 1 1 1 1 1 6 6 6 f . . .
                    . . c c c c c c c c c f . . . .
        """),
        SpriteKind.enemy)
    mySprite3.set_position(randint(40, scene.screen_width()),
        randint(40, scene.screen_height()))
    mySprite3.follow(mySprite2, 50)
    animation.run_image_animation(mySprite3,
        [img("""
                . . . . c c c c c c . . . . . .
                        . . . c 6 7 7 7 7 6 c . . . . .
                        . . c 7 7 7 7 7 7 7 7 c . . . .
                        . c 6 7 7 7 7 7 7 7 7 6 c . . .
                        . c 7 c 6 6 6 6 c 7 7 7 c . . .
                        . f 7 6 f 6 6 f 6 7 7 7 f . . .
                        . f 7 7 7 7 7 7 7 7 7 7 f . . .
                        . . f 7 7 7 7 6 c 7 7 6 f c . .
                        . . . f c c c c 7 7 6 f 7 7 c .
                        . . c 7 2 7 7 7 6 c f 7 7 7 7 c
                        . c 7 7 2 7 7 c f c 6 7 7 6 c c
                        c 1 1 1 1 7 6 f c c 6 6 6 c . .
                        f 1 1 1 1 1 6 6 c 6 6 6 6 f . .
                        f 6 1 1 1 1 1 6 6 6 6 6 c f . .
                        . f 6 1 1 1 1 1 1 6 6 6 f . . .
                        . . c c c c c c c c c f . . . .
            """),
            img("""
                . . . c c c c c c . . . . . . .
                        . . c 6 7 7 7 7 6 c . . . . . .
                        . c 7 7 7 7 7 7 7 7 c . . . . .
                        c 6 7 7 7 7 7 7 7 7 6 c . . . .
                        c 7 c 6 6 6 6 c 7 7 7 c . . . .
                        f 7 6 f 6 6 f 6 7 7 7 f . . . .
                        f 7 7 7 7 7 7 7 7 7 7 f . . . .
                        . f 7 7 7 7 6 c 7 7 6 f . . . .
                        . . f c c c c 7 7 6 f c c c . .
                        . . c 6 2 7 7 7 f c c 7 7 7 c .
                        . c 6 7 7 2 7 7 c f 6 7 7 7 7 c
                        . c 1 1 1 1 7 6 6 c 6 6 6 c c c
                        . c 1 1 1 1 1 6 6 6 6 6 6 c . .
                        . c 6 1 1 1 1 1 6 6 6 6 6 c . .
                        . . c 6 1 1 1 1 1 7 6 6 c c . .
                        . . . c c c c c c c c c c . . .
            """)],
        100,
        True)
game.on_update_interval(2000, on_update_interval)

def on_forever():
    pause(1000)
    info.change_score_by(1)
forever(on_forever)
