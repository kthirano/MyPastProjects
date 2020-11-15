class r_strs:
    ILLEGAL_CHANNELS = ['general', 'assign_roles']
    ILLEGAL_ROLES = ['Admin', 'ForFunPythonApp']
    NEWROLE_1 = "React with "
    NEWROLE_2 = " to receive notificaitions when people want to play "
    NEWROLE_3 = "To use this, "
    REACTIONS = [':thumbsup:' , ':muscle:', ':eyes:' , ':yum:', ':ok_hand:', ':rice_ball:', ':trophy:', ':alien:']
    REACTION_CODE = ['\N{THUMBS UP SIGN}','\N{FLEXED BICEPS}','\N{EYES}','\N{FACE SAVOURING DELICIOUS FOOD}','\N{OK HAND SIGN}','\N{RICE BALL}','\N{TROPHY}','\N{EXTRATERRESTRIAL ALIEN}']
    CHANNEL_EXISTS = 'Channel already exists: '
    BOT_TEXTCHANNEL = 'Bot-Generated Text Channels'
    MAYTHEODDS = 'May the odds be in your favor: '
    DEFAULT_CHANNEL_NAME = 'just-chatting'
    TRYNA_BE_SNEAKY = "Wow, you think you're sooo sneaky don't you?"
    ROLE_ALREADY_EXISTS = 'Role already exists'

    @staticmethod
    def processRoleMessage(message):
        split_message = message.split()
        reaction = split_message[len(r_strs.NEWROLE_1.split())]
        reaction_code = r_strs.REACTION_CODE[r_strs.REACTIONS.index(reaction)]
        new_role = split_message[len(r_strs.NEWROLE_1.split()) + 1 + len(r_strs.NEWROLE_2.split())]
        return (reaction_code, new_role)
