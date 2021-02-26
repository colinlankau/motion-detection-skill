from mycroft import MycroftSkill, intent_file_handler


class MotionDetection(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('detection.motion.intent')
    def handle_detection_motion(self, message):
        self.speak_dialog('detection.motion')


def create_skill():
    return MotionDetection()

