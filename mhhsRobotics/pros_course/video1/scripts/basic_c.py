"""
Basic C / Programming Fundamentals -- intro animation (PROS course, video 1).

A 3Blue1Brown-style explainer that follows the recording transcript:
    1. "What happens underneath the hood?"
    2. High-level languages (Python / Go) sit on layers of abstraction.
    3. Those layers shield you from memory, system calls, drivers, hardware.
    4. Understanding the fundamentals makes you a better developer.
    5. So today: a simple introduction to C.
    6. C++ is the successor, built on C's downsides.
    7. PROS supports both C and C++.

Render with (Manim Community):
    manim -pqh basic_c.py BasicProgramming

Tuned to land around ~69s of narration. Each section is its own method so
the timing is easy to nudge against the voiceover.
"""

from manim import *


# --- palette -----------------------------------------------------------------
BG = "#0e1116"
ACCENT = "#5db4ff"     # cool blue (high-level)
WARM = "#ffb454"       # warm amber (low-level / hardware)
GREEN = "#9ece6a"
RED = "#f7768e"
MUTED = "#6b7280"
INK = "#e6e6e6"


class BasicProgramming(Scene):
    def construct(self):
        self.camera.background_color = BG

        self.scene_hood()
        self.scene_abstraction_layers()
        self.scene_shield()
        self.scene_fundamentals()
        self.scene_intro_c()
        self.scene_c_to_cpp()
        self.scene_pros_supports_both()
        self.scene_outro()

    # ------------------------------------------------------------------ #
    # 1. What happens underneath the hood?                                #
    # ------------------------------------------------------------------ #
    def scene_hood(self):
        title = Text("What happens underneath the hood?", font="sans-serif",
                     weight=BOLD, color=INK).scale(0.8)
        sub = Text("when you create a program", font="sans-serif",
                   color=MUTED).scale(0.45)
        sub.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.6)
        self.play(FadeIn(sub, shift=UP * 0.2), run_time=0.8)
        self.wait(1.0)

        group = VGroup(title, sub)
        self.play(group.animate.scale(0.55).to_edge(UP), run_time=1.0)
        self.wait(0.3)
        self.title_group = group

    # ------------------------------------------------------------------ #
    # 2. The stack of abstraction layers                                 #
    # ------------------------------------------------------------------ #
    def _layer(self, label, width, color, fill_opacity=0.18):
        rect = RoundedRectangle(corner_radius=0.12, width=width, height=0.85,
                                stroke_color=color, stroke_width=2.5,
                                fill_color=color, fill_opacity=fill_opacity)
        txt = Text(label, font="sans-serif", color=INK).scale(0.4)
        txt.move_to(rect.get_center())
        return VGroup(rect, txt)

    def scene_abstraction_layers(self):
        # Top: the languages most developers use today.
        lang = self._layer("Python   ·   Go   ·   high-level languages",
                           7.2, ACCENT, fill_opacity=0.22)

        # The hidden machinery beneath them.
        layers_def = [
            ("Memory management", ACCENT),
            ("System calls", "#7aa2f7"),
            ("Hardware drivers", WARM),
            ("Hardware", WARM),
        ]
        layers = VGroup()
        widths = [6.4, 5.8, 5.2, 4.6]
        for (label, color), w in zip(layers_def, widths):
            layers.add(self._layer(label, w, color))

        layers.arrange(DOWN, buff=0.28)
        stack = VGroup(lang, layers).arrange(DOWN, buff=0.5)
        stack.next_to(self.title_group, DOWN, buff=0.6)

        self.play(FadeIn(lang, shift=DOWN * 0.3), run_time=0.9)
        self.wait(0.4)

        brace = Brace(layers, LEFT, color=MUTED)
        brace_txt = Text("layers of\nabstraction", font="sans-serif",
                         color=MUTED).scale(0.4)
        brace_txt.next_to(brace, LEFT, buff=0.2)

        for layer in layers:
            self.play(FadeIn(layer, shift=DOWN * 0.2), run_time=0.45)
        self.play(GrowFromCenter(brace), FadeIn(brace_txt), run_time=0.8)
        self.wait(1.2)

        self.layer_stack = VGroup(stack, brace, brace_txt)
        self.lang_layer = lang
        self.hidden_layers = layers

    # ------------------------------------------------------------------ #
    # 3. The shield metaphor                                             #
    # ------------------------------------------------------------------ #
    def scene_shield(self):
        # A line slides between the language and the machinery: the shield.
        shield_line = DashedLine(
            self.lang_layer.get_left() + DOWN * 0.32 + LEFT * 0.1,
            self.lang_layer.get_right() + DOWN * 0.32 + RIGHT * 0.1,
            color=GREEN, stroke_width=3,
        )
        shield_lbl = Text("abstraction shields the developer",
                          font="sans-serif", color=GREEN).scale(0.4)
        shield_lbl.next_to(shield_line, RIGHT, buff=0.25).shift(RIGHT * 0.1)

        self.play(Create(shield_line), run_time=0.8)
        self.play(FadeIn(shield_lbl, shift=LEFT * 0.2), run_time=0.7)

        # Dim the machinery to show it's "hidden" from the developer.
        self.play(self.hidden_layers.animate.set_opacity(0.3), run_time=0.9)
        self.wait(1.2)

        self.play(
            FadeOut(self.layer_stack),
            FadeOut(shield_line),
            FadeOut(shield_lbl),
            run_time=0.9,
        )

    # ------------------------------------------------------------------ #
    # 4. Understanding the fundamentals -> better developer              #
    # ------------------------------------------------------------------ #
    def scene_fundamentals(self):
        line1 = Text("You don't need to master all of it.",
                     font="sans-serif", color=MUTED).scale(0.55)
        line2 = Text("But understanding the fundamentals",
                     font="sans-serif", color=INK).scale(0.6)
        line3 = Text("makes you a better developer",
                     font="sans-serif", weight=BOLD, color=GREEN).scale(0.65)
        line4 = Text("— and helps you understand the programs you write.",
                     font="sans-serif", color=MUTED).scale(0.45)

        block = VGroup(line1, line2, line3, line4).arrange(DOWN, buff=0.4)
        block.move_to(ORIGIN)

        self.play(FadeIn(line1, shift=UP * 0.2), run_time=0.8)
        self.wait(0.5)
        self.play(FadeIn(line2, shift=UP * 0.2), run_time=0.8)
        self.play(Write(line3), run_time=1.0)
        self.play(FadeIn(line4), run_time=0.7)
        self.wait(1.4)
        self.play(FadeOut(block), run_time=0.8)

    # ------------------------------------------------------------------ #
    # 5. A simple introduction to C                                      #
    # ------------------------------------------------------------------ #
    def scene_intro_c(self):
        big_c = Text("C", font="sans-serif", weight=BOLD,
                     color=ACCENT).scale(3.5)
        self.play(GrowFromCenter(big_c), run_time=1.0)

        caption = Text("a simple introduction to the C programming language",
                       font="sans-serif", color=INK).scale(0.5)
        caption.next_to(big_c, DOWN, buff=0.5)
        self.play(FadeIn(caption, shift=UP * 0.2), run_time=0.8)
        self.wait(0.8)

        # A tiny canonical C snippet to make it concrete.
        code = self._code_block(
            [
                '#include <stdio.h>',
                '',
                'int main(void) {',
                '    printf("Hello, robot!\\n");',
                '    return 0;',
                '}',
            ]
        )
        code.scale(0.9).next_to(caption, DOWN, buff=0.5)

        self.play(
            VGroup(big_c, caption).animate.scale(0.5).to_edge(UP, buff=1.0),
            run_time=0.9,
        )
        self.play(FadeIn(code, shift=UP * 0.3), run_time=1.0)
        self.wait(1.4)
        self.play(FadeOut(VGroup(big_c, caption, code)), run_time=0.8)

    def _code_block(self, lines):
        """Lightweight monospace 'editor' card (no external lexer needed)."""
        body = VGroup(*[
            Text(ln if ln else " ", font="monospace", color=INK).scale(0.42)
            for ln in lines
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.18)

        # crude syntax tint for keywords
        keywords = {"int", "return", "void"}
        for txt, src in zip(body, lines):
            if src.strip().startswith("#include"):
                txt.set_color(WARM)
            elif any(src.strip().startswith(k) or f" {k} " in src
                     for k in keywords):
                txt.set_color(GREEN)
            elif "printf" in src:
                txt.set_color(ACCENT)

        pad = 0.4
        card = RoundedRectangle(
            corner_radius=0.15,
            width=body.width + pad * 2,
            height=body.height + pad * 2,
            stroke_color=MUTED, stroke_width=2,
            fill_color="#161b22", fill_opacity=1.0,
        )
        body.move_to(card.get_center())
        return VGroup(card, body)

    # ------------------------------------------------------------------ #
    # 6. C -> C++ : the successor                                         #
    # ------------------------------------------------------------------ #
    def scene_c_to_cpp(self):
        c_box = self._layer("C", 2.2, ACCENT, fill_opacity=0.22).scale(1.2)
        cpp_box = self._layer("C++", 2.2, GREEN, fill_opacity=0.22).scale(1.2)

        c_box.move_to(LEFT * 3.2)
        cpp_box.move_to(RIGHT * 3.2)

        arrow = Arrow(c_box.get_right(), cpp_box.get_left(),
                      color=INK, buff=0.3, stroke_width=4)
        arrow_lbl = Text("successor", font="sans-serif",
                         color=MUTED).scale(0.4)
        arrow_lbl.next_to(arrow, UP, buff=0.2)

        self.play(FadeIn(c_box, shift=RIGHT * 0.2), run_time=0.7)
        self.play(GrowArrow(arrow), FadeIn(arrow_lbl), run_time=0.8)
        self.play(FadeIn(cpp_box, shift=LEFT * 0.2), run_time=0.7)

        note = Text("built on C's downsides to be a better language",
                    font="sans-serif", color=INK).scale(0.48)
        note.next_to(VGroup(c_box, cpp_box), DOWN, buff=1.0)
        self.play(FadeIn(note, shift=UP * 0.2), run_time=0.8)
        self.wait(1.6)

        self.play(FadeOut(VGroup(c_box, cpp_box, arrow, arrow_lbl, note)),
                  run_time=0.8)

    # ------------------------------------------------------------------ #
    # 7. PROS supports both                                              #
    # ------------------------------------------------------------------ #
    def scene_pros_supports_both(self):
        pros = Text("PROS", font="sans-serif", weight=BOLD,
                    color=WARM).scale(1.6)
        pros.to_edge(UP, buff=1.6)

        c_chip = self._layer("C", 2.0, ACCENT, fill_opacity=0.22)
        cpp_chip = self._layer("C++", 2.0, GREEN, fill_opacity=0.22)
        chips = VGroup(c_chip, cpp_chip).arrange(RIGHT, buff=1.2)
        chips.next_to(pros, DOWN, buff=1.0)

        a1 = Arrow(pros.get_bottom(), c_chip.get_top(),
                   color=MUTED, buff=0.25, stroke_width=3)
        a2 = Arrow(pros.get_bottom(), cpp_chip.get_top(),
                   color=MUTED, buff=0.25, stroke_width=3)

        self.play(Write(pros), run_time=0.9)
        self.play(GrowArrow(a1), GrowArrow(a2), run_time=0.7)
        self.play(FadeIn(c_chip, shift=UP * 0.2),
                  FadeIn(cpp_chip, shift=UP * 0.2), run_time=0.8)

        check = Text("supports both", font="sans-serif", weight=BOLD,
                     color=GREEN).scale(0.6)
        check.next_to(chips, DOWN, buff=0.9)
        self.play(FadeIn(check, shift=UP * 0.2), run_time=0.7)
        self.wait(1.6)

        self.play(FadeOut(VGroup(pros, chips, a1, a2, check)), run_time=0.8)

    # ------------------------------------------------------------------ #
    # Outro                                                              #
    # ------------------------------------------------------------------ #
    def scene_outro(self):
        outro = Text("Let's get started.", font="sans-serif",
                     weight=BOLD, color=INK).scale(0.9)
        self.play(Write(outro), run_time=1.2)
        self.wait(1.2)
        self.play(FadeOut(outro), run_time=0.9)
