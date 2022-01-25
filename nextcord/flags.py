from .types.base_flag import IntFlags, flag_value


class Intents(IntFlags):
    """
    The intents you can connect to the gateway with.

    .. note::
        See the `documentation <https://discord.dev/topics/gateway#gateway-intents>`_
    """

    flags = (
        "GUILDS",
        "GUILD_MEMBERS",
        "GUILD_BANS",
        "GUILD_EMOJIS_AND_STICKERS",
        "GUILD_INTERACTIONS",
        "GUILD_WEBHOOKS",
        "GUILD_INVITES",
        "GUILD_VOICE_STATES",
        "GUILD_PRESENCES",
        "GUILD_MESSAGES",
        "GUILD_MESSAGE_REACTIONS",
        "GUILD_MESSAGE_TYPING",
        "DIRECT_MESSAGES",
        "DIRECT_MESSAGE_REACTIONS",
        "DIRECT_MESSAGE_TYPING",
        "GUILD_SCHEDULED_EVENTS",
    )

    GUILDS = flag_value(1 << 0)
    GUILD_MEMBERS = flag_value(1 << 1)
    GUILD_BANS = flag_value(1 << 2)
    GUILD_EMOJIS_AND_STICKERS = flag_value(1 << 3)
    GUILD_INTEGRATIONS = flag_value(1 << 4)
    GUILD_WEBHOOKS = flag_value(1 << 5)
    GUILD_INVITES = flag_value(1 << 6)
    GUILD_VOICE_STATES = flag_value(1 << 7)
    GUILD_PRESENCES = flag_value(1 << 8)
    GUILD_MESSAGES = flag_value(1 << 9)
    GUILD_MESSAGE_REACTIONS = flag_value(1 << 10)
    GUILD_MESSAGE_TYPING = flag_value(1 << 11)
    DIRECT_MESSAGES = flag_value(1 << 12)
    DIRECT_MESSAGE_REACTIONS = flag_value(1 << 13)
    DIRECT_MESSAGE_TYPING = flag_value(1 << 14)
    GUILD_SCHEDULED_EVENTS = flag_value(1 << 16)


class PermissionsFlags(IntFlags):
    """
    The permissions represented in a guild.

    .. note::
        See the `documentation <https://discord.dev/topics/permissions#permissions>`_
    """

    flags = (
        "ADD_REACTIONS",
        "ADMINISTRATOR",
        "ATTACH_FILES",
        "BAN_MEMBERS",
        "CHANGE_NICKNAME",
        "CONNECT",
        "CREATE_INSTANT_INVITE",
        "CREATE_PRIVATE_THREADS",
        "CREATE_PUBLIC_THREADS",
        "DEAFEN_MEMBERS",
        "EMBED_LINKS",
        "KICK_MEMBERS",
        "MANAGE_CHANNELS",
        "MANAGE_EMOJIS_AND_STICKERS",
        "MANAGE_EVENTS",
        "MANAGE_GUILD",
        "MANAGE_MESSAGES",
        "MANAGE_NICKNAMES",
        "MANAGE_ROLES",
        "MANAGE_THREADS",
        "MANAGE_WEBHOOKS",
        "MENTION_EVERYONE",
        "MODERATE_MEMBERS",
        "MOVE_MEMBERS",
        "MUTE_MEMBERS",
        "PRIORITY_SPEAKER",
        "READ_MESSAGE_HISTORY",
        "REQUEST_TO_SPEAK",
        "SEND_MESSAGES",
        "SEND_MESSAGES_IN_THREADS",
        "SEND_TTS_MESSAGES",
        "SPEAK",
        "START_EMBEDDED_ACTIVITIES",
        "STREAM",
        "USE_APPLICATION_COMMANDS",
        "USE_EXTERNAL_EMOJIS",
        "USE_EXTERNAL_STICKERS",
        "USE_VAD",
        "VIEW_AUDIT_LOG",
        "VIEW_CHANNEL",
        "VIEW_GUILD_INSIGHTS",
    )
    CREATE_INSTANT_INVITE = flag_value(1 << 0)
    KICK_MEMBERS = flag_value(1 << 1)
    BAN_MEMBERS = flag_value(1 << 2)
    ADMINISTRATOR = flag_value(1 << 3)
    MANAGE_CHANNELS = flag_value(1 << 4)
    MANAGE_GUILD = flag_value(1 << 5)
    ADD_REACTIONS = flag_value(1 << 6)
    VIEW_AUDIT_LOG = flag_value(1 << 7)
    PRIORITY_SPEAKER = flag_value(1 << 8)
    STREAM = flag_value(1 << 9)
    VIEW_CHANNEL = flag_value(1 << 10)
    SEND_MESSAGES = flag_value(1 << 11)
    SEND_TTS_MESSAGES = flag_value(1 << 12)
    MANAGE_MESSAGES = flag_value(1 << 13)
    EMBED_LINKS = flag_value(1 << 14)
    ATTACH_FILES = flag_value(1 << 15)
    READ_MESSAGE_HISTORY = flag_value(1 << 16)
    MENTION_EVERYONE = flag_value(1 << 17)
    USE_EXTERNAL_EMOJIS = flag_value(1 << 18)
    VIEW_GUILD_INSIGHTS = flag_value(1 << 19)
    CONNECT = flag_value(1 << 20)
    SPEAK = flag_value(1 << 21)
    MUTE_MEMBERS = flag_value(1 << 22)
    DEAFEN_MEMBERS = flag_value(1 << 23)
    MOVE_MEMBERS = flag_value(1 << 24)
    USE_VAD = flag_value(1 << 25)
    CHANGE_NICKNAME = flag_value(1 << 26)
    MANAGE_NICKNAMES = flag_value(1 << 27)
    MANAGE_ROLES = flag_value(1 << 28)
    MANAGE_WEBHOOKS = flag_value(1 << 29)
    MANAGE_EMOJIS_AND_STICKERS = flag_value(1 << 30)
    USE_APPLICATION_COMMANDS = flag_value(1 << 31)
    REQUEST_TO_SPEAK = flag_value(1 << 32)
    MANAGE_EVENTS = flag_value(1 << 33)
    MANAGE_THREADS = flag_value(1 << 34)
    CREATE_PUBLIC_THREADS = flag_value(1 << 35)
    CREATE_PRIVATE_THREADS = flag_value(1 << 36)
    USE_EXTERNAL_STICKERS = flag_value(1 << 37)
    SEND_MESSAGES_IN_THREADS = flag_value(1 << 38)
    START_EMBEDDED_ACTIVITIES = flag_value(1 << 39)
    MODERATE_MEMBERS = flag_value(1 << 40)


if __name__ == "__main__":
    print(dir(Permissions))
