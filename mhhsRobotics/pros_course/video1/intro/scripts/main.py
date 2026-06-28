from manim import *


class main(Scene):
    def construct(self):

        #intro section

        self.wait(1)

        code = Code(
            code_string="print('Hello World')",
            language="python",
            formatter_style="monokai",
            background_config={"buff": .5},
            add_line_numbers=False,
        )

        self.wait(1)

        self.play(Write(code))


        self.play(code.animate.set_opacity(.2))

        arrow = Arrow(start=UP,end=DOWN/4,color=GOLD,max_stroke_width_to_length_ratio=3)
        arrow.move_to([0,1,0])

        self.play(Write(arrow),code.animate.move_to([0,2.1,0]))

        binary = Text(
            text="01101000 01100101 01101100 01101100\n 01101111 00100000 01110111 01110111 \n01110010 01101100 01100100 00100001",font_size=DEFAULT_FONT_SIZE/1.5,
            font="DejaVu Sans Mono",
        ).move_to([0,0,0])

        self.play(Write(binary))

        self.wait(.4)

        self.play(FadeOut(arrow,code,binary))


        python_logo = ImageMobject("../../../assets/logos/python_logo.png").move_to([-1.5,0,0]).scale(.5)
        self.play(FadeIn(python_logo),run_time = .5)

        self.wait(.5)

        go_logo = ImageMobject("../../../assets/logos/go_logo.png").move_to([1.5,0,0])
        self.play(FadeIn(go_logo),run_time=.5)

        self.wait(2)

        logo_group = Group()
        logo_group.add(python_logo, go_logo)

        self.wait(1.5)

        self.play(logo_group.animate.move_to([0,2,0]),Write(arrow))

        abstraction = Text(text="Abstraction")

        self.play(Write(abstraction))

        arrow2 = arrow.copy()

        self.play(arrow2.animate.move_to([0,-1,0]))

        mem = Text(text="Memory Management",color=GRAY,font_size=DEFAULT_FONT_SIZE/2).move_to([-5,-2,0])
        hardwareDrivers = Text(text="Hardware Drivers",color=GRAY,font_size=DEFAULT_FONT_SIZE/2).move_to([0,-2,0])
        Syscalls = Text(text="Syscalls",color=GRAY,font_size=DEFAULT_FONT_SIZE/2).move_to([5,-2,0])

        membox = SurroundingRectangle(mem,color=RED)
        hdbox = SurroundingRectangle(hardwareDrivers,color=RED)
        sysbox = SurroundingRectangle(Syscalls,color=RED)

        self.play(Write(mem),ShowPassingFlash(membox),run_time=1)
        self.play(Write(hardwareDrivers),ShowPassingFlash(hdbox),run_time=1)
        self.play(Write(Syscalls),ShowPassingFlash(sysbox),run_time=1)

        self.wait(2)

        self.play(Unwrite(abstraction),Unwrite(arrow2),Unwrite(arrow),Unwrite(mem),Unwrite(hardwareDrivers),Unwrite(Syscalls))
        self.play(FadeOut(logo_group))

        self.wait(1.5)


        cpp_code = Code(
            code_file="../../../../../../MHHS_Robotics/shockwave_code/pushback_shockwave/src/main.cpp",
            language="cpp",
            formatter_style="monokai",
            add_line_numbers=False,
            background="window",
        ).scale(.5)

        cpp_code.to_edge(UP)


        self.play(Write(cpp_code))

        scroll = cpp_code.height - config.frame_height+1
        self.play(cpp_code.animate.shift(UP*scroll),run_time=7,rate_func=smooth)

        self.wait(1)

        self.play(FadeOut(cpp_code),run_time=.75)

        c_logo = ImageMobject("../../../assets/logos/c_logo.png")
        cpp_logo = ImageMobject("../../../assets/logos/cpp_logo.png")

        self.play(FadeIn(c_logo))

        self.wait(1)

        self.play(c_logo.animate.move_to([-2,0,0]).scale(.5))

        self.wait(1)

        self.play(FadeIn(cpp_logo))

        self.wait(1)

        self.play(cpp_logo.animate.move_to([2,0,0]).scale(.5))

        arrow = Arrow(start=LEFT, end=RIGHT, stroke_width=10, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=.25).move_to([0,0,0])
        predecessor = Text(text="Predecessor",font_size=DEFAULT_FONT_SIZE/2).move_to([-2,1,0])
        self.play(Write(arrow), Write(predecessor))

        redarrow = Arrow(start=UP, end=DOWN, stroke_width=10, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=1,color=RED).move_to([-3,0,0])
        redarrow.scale(.5)

        self.wait(1)

        self.play(Write(redarrow),run_time=1)

        curvedarrow = CurvedArrow(start_point=[-3,-.5,0],end_point=[3,-.5,0],color=BLUE)

        self.play(Write(curvedarrow))

        greenArrow = Arrow(start=DOWN, end=UP, stroke_width=10, max_stroke_width_to_length_ratio=100, max_tip_length_to_length_ratio=1,color=GREEN).move_to([3,0,0])
        greenArrow.scale(.5)

        self.play(Write(greenArrow),run_time=2)

        self.wait(1)

        self.play(FadeOut(greenArrow,redarrow,arrow,curvedarrow, cpp_logo, c_logo,predecessor))

        brain = SVGMobject("../../../assets/other_images/brain.svg",color=WHITE).set_opacity(1)
        brain.set_fill(WHITE)

        self.play(DrawBorderThenFill(brain),run_time=3,rate_func=smooth)

        self.play(brain.animate.move_to([0,2,0]),run_time=1)

        c_logo.move_to([0,0,0])

        self.play(LaggedStart(ShowIncreasingSubsets(c_logo),c_logo.animate.move_to([3,0,0])),run_time=1)

        self.play(c_logo.animate.set_opacity(.7).move_to([3,1,0]))

        c_code = Code(
            code_file = "c.c",
            formatter_style= "emacs",
            language="c",
            tab_width=8,
            background="window",
        ).move_to([3,-2,0]).scale(.8).set_opacity(.8)

        cpp_code = Code(
            code_file = "cpp.cpp",
            formatter_style= "emacs",
            language = "cpp",
            tab_width=8,
            background="window",    
        ).move_to([-3,-2,0]).scale(.8).set_opacity(.4)

        self.play(Write(c_code),run_time=1)

        self.play(c_code.animate.move_to([0,2,0]),c_logo.animate.move_to([0,2,0]),run_time=1)
        self.play(c_code.animate.scale(0),c_logo.animate.scale(0))
        self.play(FadeOut(c_code),FadeOut(c_logo))


        self.play(ShowIncreasingSubsets(cpp_logo), cpp_logo.animate.move_to([-3,0,0]),run_time=1)
        self.play(cpp_logo.animate.set_opacity(.7).move_to([-3,1,0]),brain.animate.move_to([2,-.5,0]),Write(cpp_code),run_time=1)

        bulb = ImageMobject(
            "../../../assets/other_images/lightbulb.png",
        ).move_to([1,1,0]).scale(.3).set_opacity(1)

        igetitText = Text(
            text="Looks a little familiar..",
            font_size=DEFAULT_FONT_SIZE/1.3,
        ).move_to([3.3,1,0]).scale(.7)

        self.play(FadeIn(bulb))
        self.play(Write(igetitText))

        self.wait(2)

        self.play(FadeOut(cpp_logo),FadeOut(brain),FadeOut(cpp_code),FadeOut(bulb),FadeOut(igetitText))