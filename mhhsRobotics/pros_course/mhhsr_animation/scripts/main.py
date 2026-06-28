from manim import *

class main(Scene):
    def construct(self):

        MHHSR_logo = ImageMobject("../../assets/logos/mhhsr-logo-transparent.png").scale(.15)

        self.play(FadeIn(MHHSR_logo,run_time=4,rate_func=rate_functions.ease_in_quint))

        self.wait(1)

        self.play(MHHSR_logo.animate(run_time=2).set_opacity(.3))

        text = Text("MHHS Robotics").scale(1.25)

        self.play(Write(text))