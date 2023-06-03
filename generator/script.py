import moviepy.editor as mpy
from moviepy.video.tools.segmenting import findObjects


class UserVideo:
    BACKGROUND = (124, 252, 0)
    SCREEN_SIZE = (100, 100)
    t = 3

    def __init__(self, txt: str):
        self.txt = txt

    def text_position_func(self, t):
        return -(t/3) * len(self.txt) * 25, 'center'

    def video_maker(self):
        txt_clip = mpy.TextClip(
                self.txt,
                font="Amiri-Bold",
                color="White",
                kerning=2,
                fontsize=50,
        ).set_position(lambda t: self.text_position_func(t))

        created_video = (
            mpy.CompositeVideoClip([txt_clip], size=self.SCREEN_SIZE)
            .on_color(color=self.BACKGROUND, col_opacity=1)
            .set_duration(self.t)
        )
        user_video = created_video.write_videofile(f"{self.txt}.mp4", fps=60)
        return user_video