from manim import *

class main(ThreeDScene):
    def construct(self):

        varText = Text("Variables",color=MAROON).scale(2)

        self.play(Write(varText))

        self.wait(1.5)

        self.play(FadeOut(varText),run_time=2)

        var1 = Variable(0, "x", var_type = Integer).move_to([-1.5,0,0])
        var2 = Variable(0, "x", var_type = Integer).move_to([1.5,0,0])

        c_logo = ImageMobject("../../../assets/logos/c_logo.png").move_to([-2,1.5,0]).scale(.5)
        py_logo = ImageMobject("../../../assets/logos/py_logo.png").move_to([2,1.5,0]).scale(.5)
        equals = Text("=").move_to([0,0,0])
        ebox = SurroundingRectangle(equals)

        self.play(FadeIn(c_logo),FadeIn(py_logo))
        self.play(Write(var1),Write(var2))
        self.wait(1)

        self.play(var1.tracker.animate.set_value(10),var2.tracker.animate.set_value(10), run_time=1)
        self.play(var1.tracker.animate.set_value(5),var2.tracker.animate.set_value(5),Write(equals),ShowPassingFlash(ebox),run_time=1)
        self.play(var1.tracker.animate.set_value(7),var2.tracker.animate.set_value(7),rate_func=smooth)
        self.play(FadeOut(var2,var1,c_logo,py_logo,equals))

        self.set_camera_orientation(phi=75*DEGREES, theta=-45*DEGREES)

        axes = ThreeDAxes()
        container = Cube(side_length=1, fill_opacity=.55,fill_color=LIGHT_BROWN)
        containertext = Text("containers",slant=ITALIC).move_to([0,-1.5,0])
        self.add_fixed_in_frame_mobjects(containertext)
        containertext.set_opacity(0)

        self.play(GrowFromCenter(container),containertext.animate.set_opacity(1),rate_func=smooth)

        containers = VGroup(*[Cube(side_length=1, fill_opacity=.55,fill_color=LIGHT_BROWN) for i in range(8)]).arrange(RIGHT,buff=.5).rotate(45*DEGREES,axis=OUT)

        self.play(ReplacementTransform(container,containers))

        values = [0,1,True,False,'"str"',3.14,2.718,"'c'"]

        contents = VGroup()

        for i, c in enumerate(containers):
            txt = Text(str(values[i])).scale(.4).move_to([c.get_center()+OUT*1.5]).set_opacity(0)
            self.add_fixed_orientation_mobjects(txt)
            contents.add(txt)

        self.play(LaggedStart(*[c.animate.set_opacity(1) for c in contents],lag_ratio=.1))
        self.play(LaggedStart(*[t.animate.move_to(c.get_center()) for t, c in zip(contents, containers)],lag_ratio=.05))

        self.wait(1)

        self.play(LaggedStart(*[ShrinkToCenter(i) for i in containers]))
        self.play(FadeOut(containertext))

        # flatten camera AND line up data in one smooth motion
        self.move_camera(
            phi=0, theta=-90*DEGREES,
            added_anims=[contents.animate.arrange(RIGHT, buff=0.8).move_to(ORIGIN)],
            run_time=2,
        )

        # title at top
        dtText = Text("Datatypes").to_edge(UP)
        self.play(Write(dtText),run_time=.75)

        arrows = VGroup()

        for i in contents:
            arrow = Arrow(start=i,end=dtText.get_center()-UP*.25,stroke_width=1,max_tip_length_to_length_ratio=.1,tip_length=.15)
            arrows.add(arrow)
            self.play(Create(arrow),run_time=.05)

        intbox = SurroundingRectangle(contents[0],contents[1])
        floatbox = SurroundingRectangle(contents[5],contents[6])
        charbox = SurroundingRectangle(contents[7])
        strbox = SurroundingRectangle(contents[4])
        boolbox = SurroundingRectangle(contents[2],contents[3])

        self.play(ShowPassingFlash(intbox))
        self.wait(2)
        self.play(ShowPassingFlash(floatbox))
        self.wait(1)
        self.play(ShowPassingFlash(charbox))
        self.wait(3)
        self.play(ShowPassingFlash(strbox))
        self.wait(3)
        self.play(ShowPassingFlash(boolbox))

        self.play(FadeOut(dtText))
        self.play(FadeOut(*[i for i in contents]))
        self.play(FadeOut(*[i for i in arrows]))

        types = {

            # --- C Basic & Modified Integer Types ---
            "char", "signed char", "unsigned char",
            "short", "short int", "signed short", "unsigned short",
            "int", "signed int", "unsigned int",
            "long", "long int", "signed long", "unsigned long",
            "long long", "unsigned long long",

        }
        types2 = {
            # --- Standard & High-Level Python Types ---
            "str", "list", "tuple", "dict", "set", "frozenset", "range",
            "complex", "bytes", "bytearray", "memoryview", "NoneType", "null",

            # --- C Floating-Point Types ---
            "float", "double", "long double",
        }
        types3 = {
            # --- C Pointers ---
            "int*", "char*", "float*", "double*", "void*", 
            "int**", "char**", "void**",

            # --- C Special, Structures & Modern Types ---
            "bool", "size_t", "struct", "union", "enum", "void"
        }


        left_off  = -config.frame_width/2 - 1
        right_off =  config.frame_width/2 + 1
        speed = 1
        accel = .5

        items = VGroup(*[Text(t).scale(.5) for t in types]).arrange(RIGHT,buff=1.25)
        items.move_to([ORIGIN])
        period = items.width + 1.5

        items2 = VGroup(*[Text(t).scale(.5) for t in types2]).arrange(RIGHT,buff=1.25)
        items2.move_to([0,3,0])
        period2 = items2.width + 1.5

        items3 = VGroup(*[Text(t).scale(.5) for t in types3]).arrange(RIGHT,buff=1.25)
        items3.move_to([0,-3,0])
        period3 = items3.width + 1.5


        def scroll(group, dt):          # moves LEFT
            nonlocal speed
            speed += accel * dt
            group.shift(LEFT * speed * dt)
            for item in group:
                if item.get_right()[0] < left_off:
                    item.shift(RIGHT * period)

        def scroll2(group, dt):         # moves RIGHT
            group.shift(RIGHT * speed * dt)
            for item in group:
                if item.get_left()[0] > right_off:
                    item.shift(LEFT * period2)

        def scroll3(group, dt):         # moves RIGHT
            group.shift(RIGHT * speed * dt)
            for item in group:
                if item.get_left()[0] > right_off:
                    item.shift(LEFT * period3)


        items.add_updater(scroll)
        items2.add_updater(scroll2)
        items3.add_updater(scroll3)

        self.add(items,items2,items3)
        self.wait(10)
        self.play(FadeOut(items,items2,items3))
        items.remove_updater(scroll)
        items2.remove_updater(scroll2)
        items3.remove_updater(scroll3)


        self.wait(2)

        var1 = Variable(0, "x", var_type = Integer).move_to([-1.5,0,0])
        var2 = Variable(0, "x", var_type = Integer).move_to([1.5,0,0])

        c_logo = ImageMobject("../../../assets/logos/c_logo.png").move_to([-2,1.5,0]).scale(.5)
        py_logo = ImageMobject("../../../assets/logos/py_logo.png").move_to([2,1.5,0]).scale(.5)
        equals = Text("=").move_to([0,0,0])
        ebox = SurroundingRectangle(equals)

        self.play(FadeIn(c_logo),FadeIn(py_logo))
        self.play(Write(var1),Write(var2))
        self.wait(1)

        self.play(var1.tracker.animate.set_value(10),var2.tracker.animate.set_value(10), run_time=1)
        self.play(var1.tracker.animate.set_value(5),var2.tracker.animate.set_value(5),Write(equals),ShowPassingFlash(ebox),run_time=1)
        self.play(var1.tracker.animate.set_value(7),var2.tracker.animate.set_value(7),rate_func=smooth)
        self.play(FadeOut(var2,var1,c_logo,py_logo,equals))

        self.wait(2)

        sText = Text("Syntax",color=GREEN).move_to([0,3,0])
        cCode = Code(code_string="int i = 0;",language="c",add_line_numbers=False).move_to([-3,-1,0])
        pyCode = Code(code_string="i = 0", language="python",add_line_numbers=False).move_to([3,-1,0])

        self.play(Write(sText))

        self.play(FadeIn(c_logo),c_logo.animate.move_to([-3,1,0]),Write(cCode))
        self.play(FadeIn(py_logo),py_logo.animate.move_to([3,1,0]),Write(pyCode))

        arrow = Arrow(start=[-3,-3,0],end=[-3.5,-1,0],max_tip_length_to_length_ratio=.25,color=RED)

        self.play(Create(arrow))

        self.wait(10)

        self.play(FadeOut(c_logo,py_logo,cCode,pyCode,arrow),run_time=5)

        self.play(FadeOut(sText))

        self.wait(3)

        pText = Text("Primitive").move_to([-5,3,0])
        rText = Text("Reference").move_to([5,3,0])

        self.play(Write(pText))

        self.wait(3)

        self.play(Write(rText))

        self.wait(1.5)

        self.play(FadeOut(rText))
        self.play(pText.animate.move_to([0,3,0]),pText.animate.scale(1.25))

        hvText = MarkupText('hold/store <span fgcolor="#E71D36"><i>real values</i></span>').move_to([-1,0,0])
        
        self.play(Write(hvText))

        self.wait(1.5)

        pdata = [0,3.14,True,"'c'",'"string"']
        pobjects = []

        for index, data in enumerate(pdata):
            dText = Text(str(data),color=BLUE_B).move_to([index*2-3,-1.5,0])
            self.play(Write(dText))
            pobjects.append(dText)

        self.wait(8)

        for i in pobjects:
            self.play(FadeOut(i),run_time=.2)
        self.play(FadeOut(dText,pText,hvText))
        
        self.play(FadeIn(rText),rText.animate.scale(1.25))

        haText = MarkupText("hold/store <span fgcolor='#E71D36'> <i> memory addresses </i></span>").move_to([-1,0,0])
        self.play(Write(haText),run_time=2)

        addy = MarkupText("not <span fgcolor='#1A5E63'><i> 0 </i></span>, but where <span fgcolor='#1A5E63'><i>0 lives</i></span> in memory",color=TEAL_E).move_to([0,-2.5,0])
        self.play(Write(addy),run_time=2)

        self.wait(20)

        self.play(FadeOut(haText,rText,addy))
        

