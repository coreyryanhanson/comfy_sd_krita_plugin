from krita import QPushButton

from ..script import script
from ..widgets import TipsLayout
from .img_base import SDImgPageBase
from ..utils import get_workflow

class Img2ImgPage(SDImgPageBase):
    name = "Img2Img"

    def __init__(self, *args, **kwargs):
        super(Img2ImgPage, self).__init__(cfg_prefix="img2img", *args, **kwargs)

        self.btn = QPushButton("Start img2img")
        self.get_workflow_btn = QPushButton("Get workflow")

        self.tips = TipsLayout(
            ["Select what you want the model to perform img2img on."]
        )

        self.layout.addLayout(self.denoising_strength_layout)
        self.layout.addWidget(self.btn)
        self.layout.addWidget(self.get_workflow_btn)
        self.layout.addLayout(self.tips)
        self.layout.addStretch()

    def cfg_init(self):
        super(Img2ImgPage, self).cfg_init()

        self.tips.setVisible(not script.cfg("minimize_ui", bool))

    def cfg_connect(self):
        super(Img2ImgPage, self).cfg_connect()
        self.btn.released.connect(lambda: script.action_img2img())
        self.get_workflow_btn.released.connect(
            lambda: get_workflow(script.cfg, script.action_get_workflow, "img2img")
        )
