# Copyright 2017 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from transliteration import getInstance
import io
#import websocket

logger = getLogger(__name__)


class PersonalSkill(MycroftSkill):

    def __init__(self):
        super(PersonalSkill, self).__init__(name="PersonalSkill")

    def initialize(self):
        when_were_you_born_intent = IntentBuilder("WhenWereYouBornIntent")\
            .require("WhenWereYouBornKeyword").build()
        self.register_intent(when_were_you_born_intent,
                             self.handle_when_were_you_born_intent)

        where_were_you_born_intent = IntentBuilder("WhereWereYouBornIntent")\
            .require("WhereWereYouBornKeyword").build()
        self.register_intent(where_were_you_born_intent,
                             self.handle_where_were_you_born_intent)

        who_made_you_intent = IntentBuilder("WhoMadeYouIntent")\
            .require("WhoMadeYouKeyWord").build()
        self.register_intent(who_made_you_intent,
                             self.handle_who_made_you_intent)

        who_are_you_intent = IntentBuilder("WhoAreYouIntent")\
            .require("WhoAreYouKeyword").build()
        self.register_intent(who_are_you_intent,
                             self.handle_who_are_you_intent)

        what_are_you_intent = IntentBuilder("WhatAreYouIntent")\
            .require("WhatAreYouKeyword").build()
        self.register_intent(what_are_you_intent,
                             self.handle_what_are_you_intent)

	self.add_event('speak', self.catch_speaking)

    def handle_when_were_you_born_intent(self, message):
	fp=open("/home/saurabhpanjwani5/result/2.txt","r+")
	fp.truncate()
        self.speak_dialog("when.was.i.born")

    def handle_where_were_you_born_intent(self, message):
	fp=open("/home/saurabhpanjwani5/result/2.txt","r+")
	fp.truncate()
        self.speak_dialog("where.was.i.born")

    def handle_who_made_you_intent(self, message):
	fp=open("/home/saurabhpanjwani5/result/2.txt","r+")
	fp.truncate()
        self.speak_dialog("who.made.me")

    def handle_who_are_you_intent(self, message):
	fp=open("/home/saurabhpanjwani5/result/2.txt","r+")
	fp.truncate()
        name = self.config_core.get("listener", {}).get("wake_word",
                                                        "mycroft")
        name = name.lower().replace("hey ", "")
        self.speak_dialog("who.am.i", {"name": name})

    def handle_what_are_you_intent(self, message):
	fp=open("/home/saurabhpanjwani5/result/2.txt","r+")
	fp.truncate()
        self.speak_dialog("what.am.i")

    def catch_speaking(self, message):
	#f = io.open("/home/saurabhpanjwani5/result/2.txt", 'a', encoding='utf8')
	f=open("/home/saurabhpanjwani5/result/2.txt","a")
    	dict = message.data
   	to_speak = dict.get('utterance')
	lang = dict.get('lang')
	t = getInstance()
	#new_text=unicode(to_speak,encoding="utf-8")
	#new_text=to_speak.decode("utf-8")
	t_text = t.transliterate(to_speak, "en_IN")
	
	if isinstance(t_text,unicode):
		t_text=t_text.encode('utf8')

	f.write(t_text)
	f.write("\n")
   	# do whatever you want from here
   	# for example, to show everything Mycroft speaks on the Mark 1 faceplate:
   	#self.enclosure.mouth_text(to_speak)


    def stop(self):
        pass


def create_skill():
    return PersonalSkill()
