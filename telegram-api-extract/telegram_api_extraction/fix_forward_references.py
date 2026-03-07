#!/usr/bin/env python3
"""
Fix forward references in telegram_api modules by quoting cross-module types.

This script ensures that all type references from other modules are quoted
as string annotations to avoid circular import issues.
"""

import re
from pathlib import Path
from typing import Dict, Set, List, Tuple


# Define which types belong to which module
MODULE_TYPE_MAP = {
    # types module - core types
    'types': {
        'User', 'Chat', 'Message', 'MessageEntity', 'CallbackQuery',
        'ChatMember', 'ChatMemberUpdated', 'ChatMemberOwner', 'ChatMemberAdministrator',
        'ChatMemberMember', 'ChatMemberRestricted', 'ChatMemberLeft', 'ChatMemberBanned',
        'ChatMemberPhoto', 'BotCommand', 'BotCommandScope', 'BotCommandScopeDefault',
        'BotCommandScopeAllPrivateChats', 'BotCommandScopeAllGroupChats',
        'BotCommandScopeAllChatAdministrators', 'BotCommandScopeChat',
        'BotCommandScopeChatAdministrators', 'BotCommandScopeChatMember',
        'BotCommandScopeAllChatAdministrators', 'BotCommandScopeAllGroupChats',
        'BotCommandScopeAllPrivateChats', 'BotCommandScopeDefault',
        'BotInfo', 'PhotoSize', 'Animation', 'Audio', 'Document', 'Video',
        'VideoNote', 'Voice', 'Contact', 'Dice', 'Poll', 'PollOption',
        'PollAnswer', 'Location', 'Venue', 'WebAppData', 'ProximityAlertTriggered',
        'MessageAutoDeleteTimerChanged', 'ChatShared', 'UsersShared', 'ChatInviteLink',
        'ChatAdministratorRights', 'VideoChatStarted', 'VideoChatEnded',
        'VideoChatParticipantsInvited', 'VideoChatScheduled', 'GiveawayCreated',
        'Giveaway', 'GiveawayWinners', 'GiveawayCompleted', 'ChatBoostAdded',
        'BackgroundFill', 'BackgroundFillFreeformGradient', 'BackgroundFillGradient',
        'BackgroundFillSolid', 'ChatBackground', 'ForumTopicCreated', 'ForumTopicEdited',
        'ForumTopicClosed', 'ForumTopicReopened', 'GeneralForumTopicHidden',
        'GeneralForumTopicUnhidden', 'SharedUser', 'WebAppInfo', 'KeyboardButton',
        'ReplyKeyboardMarkup', 'ReplyKeyboardRemove', 'InlineKeyboardMarkup',
        'InlineKeyboardButton', 'LoginUrl', 'SwitchInlineQueryChosenChat',
        'CallbackGame', 'ForceReply', 'ChatPhoto', 'ChatInviteLink',
        'ChatAdministratorRights', 'ChatPermissions', 'BotName',
        'BotDescription', 'BotShortDescription', 'MenuButton', 'MenuButtonCommands',
        'MenuButtonWebApp', 'MenuButtonDefault', 'ChatBoostSourcePremium',
        'ChatBoostSourceGiftCode', 'ChatBoostSourceGiveaway', 'ChatBoost',
        'ChatBoostUpdated', 'ChatBoostRemoved', 'UserChatBoosts',
        'ChatBoostSource', 'BusinessConnectionId', 'BusinessMessagesDeleted',
        'BusinessConnection', 'BusinessIntro', 'BusinessLocation', 'BusinessOpeningHours',
        'BusinessOpeningHoursInterval', 'InputMediaPhoto', 'InputMediaVideo',
        'InputMediaAnimation', 'InputMediaAudio', 'InputMediaDocument',
        'InputPaidMediaPhoto', 'InputPaidMediaVideo', 'InputPaidMedia',
        'PaidMediaInfo', 'PaidMediaPreview', 'PaidMedia', 'RevenueWithdrawalState',
        'RevenueWithdrawalStatePending', 'RevenueWithdrawalStateSucceeded',
        'RevenueWithdrawalStateFailed', 'StarTransaction', 'TransactionPartner',
        'TransactionPartnerUser', 'TransactionPartnerFragment', 'TransactionPartnerTelegramAds',
        'TransactionPartnerOther', 'ReplyParameters', 'ExternalReplyInfo',
        'TextQuote', 'LinkPreviewOptions', 'UserProfilePhotos', 'ChatPhoto',
        'ChatInviteLink', 'ChatFullInfo', 'SentWebAppMessage', 'Story',
        'SentWebAppMessage', 'InaccessibleMessage', 'WriteAccessAllowed',
        'PassportData', 'EncryptedPassportElement', 'EncryptedCredentials',
        'PassportFile', 'PassportElementError', 'PassportElementErrorDataField',
        'PassportElementErrorFrontSide', 'PassportElementErrorReverseSide',
        'PassportElementErrorSelfie', 'PassportElementErrorFile',
        'PassportElementErrorFiles', 'PassportElementErrorTranslationFile',
        'PassportElementErrorTranslationFiles', 'PassportElementErrorUnspecified',
        'SecureValue', 'SecureData', 'SecureValueType', 'IdDocumentData',
        'ResidentialAddress', 'PersonalDetails', 'Passport', 'DriverLicense',
        'IdentityCard', 'InternalPassport', 'Address', 'UtilityBill', 'BankStatement',
        'RentalAgreement', 'PassportRegistration', 'TemporaryRegistration',
        'PhoneNumber', 'Email', 'OrderInfo', 'ShippingAddress', 'LabeledPrice',
        'Invoice', 'ShippingOption', 'SuccessfulPayment', 'ShippingQuery',
        'PreCheckoutQuery', 'Game', 'GameHighScore', 'CallbackGame',
        'Animation', 'Audio', 'Document', 'PhotoSize', 'Sticker',
        'Video', 'VideoNote', 'Voice', 'Contact', 'Dice', 'PollOption',
        'PollAnswer', 'Location', 'Venue', 'Invoice', 'SuccessfulPayment',
        'LabeledPrice', 'ShippingAddress', 'ShippingOption', 'OrderInfo',
        'ShippingQuery', 'PreCheckoutQuery', 'Game', 'GameHighScore',
        'PassportData', 'EncryptedPassportElement', 'EncryptedCredentials',
        'PassportFile', 'PassportElementError', 'SecureValue', 'SecureData',
        'WebAppData', 'InlineQuery', 'InlineQueryResultsButton',
        'InlineQueryResultArticle', 'InlineQueryResultPhoto', 'InlineQueryResultVideo',
        'InlineQueryResultAudio', 'InlineQueryResultVoice', 'InlineQueryResultDocument',
        'InlineQueryResultLocation', 'InlineQueryResultVenue', 'InlineQueryResultContact',
        'InlineQueryResultGame', 'InlineQueryResultCachedPhoto', 'InlineQueryResultCachedVideo',
        'InlineQueryResultCachedAudio', 'InlineQueryResultCachedVoice',
        'InlineQueryResultCachedDocument', 'InlineQueryResultCachedSticker',
        'InlineQueryResultCachedGif', 'InlineQueryResultCachedMpeg4Gif',
        'InlineQueryResultCachedPhoto', 'InlineQueryResultCachedSticker',
        'InlineQueryResultCachedVideo', 'InlineQueryResultCachedVoice',
        'InlineQueryResultCachedAudio', 'InlineQueryResultCachedDocument',
        'ChosenInlineResult', 'InputMedia', 'InputMediaPhoto', 'InputMediaVideo',
        'InputMediaAnimation', 'InputMediaAudio', 'InputMediaDocument',
        'InputTextMessageContent', 'InputLocationMessageContent', 'InputVenueMessageContent',
        'InputContactMessageContent', 'InputInvoiceMessageContent', 'InputPollOption',
        'SentWebAppMessage', 'LabeledPrice', 'Invoice', 'ShippingAddress',
        'ShippingOption', 'SuccessfulPayment', 'ShippingQuery', 'PreCheckoutQuery',
        'RefundedPayment', 'OrderInfo', 'ShippingAddress', 'Game', 'CallbackGame',
        'GameHighScore', 'StickerSet', 'Sticker', 'MaskPosition', 'InputSticker',
        'InlineQuery', 'ChosenInlineResult', 'InlineQueryResultArticle',
        'InlineQueryResultPhoto', 'InlineQueryResultVideo', 'InlineQueryResultAudio',
        'InlineQueryResultVoice', 'InlineQueryResultDocument', 'InlineQueryResultLocation',
        'InlineQueryResultVenue', 'InlineQueryResultContact', 'InlineQueryResultGame',
        'InputTextMessageContent', 'InputLocationMessageContent', 'InputVenueMessageContent',
        'InputContactMessageContent', 'InputInvoiceMessageContent',
    },

    # methods module - just methods, no types
    'methods': set(),

    # getting_updates module
    'getting_updates': {
        'Update', 'WebhookInfo',
    },

    # stickers module
    'stickers': {
        'StickerSet', 'Sticker', 'MaskPosition', 'InputSticker',
    },

    # inline_mode module
    'inline_mode': {
        'InlineQuery', 'InlineQueryResultsButton',
        'InlineQueryResultArticle', 'InlineQueryResultPhoto', 'InlineQueryResultVideo',
        'InlineQueryResultAudio', 'InlineQueryResultVoice', 'InlineQueryResultDocument',
        'InlineQueryResultLocation', 'InlineQueryResultVenue', 'InlineQueryResultContact',
        'InlineQueryResultGame', 'InlineQueryResultCachedPhoto', 'InlineQueryResultCachedVideo',
        'InlineQueryResultCachedAudio', 'InlineQueryResultCachedVoice',
        'InlineQueryResultCachedDocument', 'InlineQueryResultCachedSticker',
        'InlineQueryResultCachedGif', 'InlineQueryResultCachedMpeg4Gif',
        'ChosenInlineResult', 'InputTextMessageContent', 'InputLocationMessageContent',
        'InputVenueMessageContent', 'InputContactMessageContent', 'InputInvoiceMessageContent',
    },

    # payments module
    'payments': {
        'LabeledPrice', 'Invoice', 'ShippingAddress', 'ShippingOption',
        'SuccessfulPayment', 'ShippingQuery', 'PreCheckoutQuery', 'RefundedPayment',
        'OrderInfo',
    },

    # passport module
    'passport': {
        'PassportData', 'EncryptedPassportElement', 'EncryptedCredentials',
        'PassportFile', 'PassportElementError', 'PassportElementErrorDataField',
        'PassportElementErrorFrontSide', 'PassportElementErrorReverseSide',
        'PassportElementErrorSelfie', 'PassportElementErrorFile',
        'PassportElementErrorFiles', 'PassportElementErrorTranslationFile',
        'PassportElementErrorTranslationFiles', 'PassportElementErrorUnspecified',
        'SecureValue', 'SecureData',
    },

    # games module
    'games': {
        'Game', 'GameHighScore', 'CallbackGame',
    },

    # updating_messages module - methods only
    'updating_messages': set(),
}


def get_type_module(type_name: str) -> str:
    """Determine which module a type belongs to."""
    for module, types_set in MODULE_TYPE_MAP.items():
        if type_name in types_set:
            return module
    return None


def is_primitive_type(type_str: str) -> bool:
    """Check if a type string is a primitive type."""
    primitives = {'int', 'str', 'bool', 'float', 'None', 'Any', 'True', 'False'}
    type_str = type_str.strip()

    # Handle union types
    if '|' in type_str:
        parts = [p.strip() for p in type_str.split('|')]
        return all(is_primitive_type(p) for p in parts)

    # Handle list types
    if type_str.startswith('list[') and type_str.endswith(']'):
        inner = type_str[5:-1].strip()
        return is_primitive_type(inner)

    return type_str in primitives


def should_quote_type(type_str: str, current_module: str) -> bool:
    """Determine if a type annotation should be quoted."""
    type_str = type_str.strip()

    # If it's a primitive type, don't quote
    if is_primitive_type(type_str):
        return False

    # If it's already quoted, don't quote again
    if type_str.startswith('"') and type_str.endswith('"'):
        return False

    # Handle None | Type syntax
    if '|' in type_str:
        parts = [p.strip() for p in type_str.split('|')]
        # If any part is a non-primitive type, quote the whole thing
        for part in parts:
            if not is_primitive_type(part):
                # Check if this type belongs to another module
                type_module = get_type_module(part)
                if type_module and type_module != current_module:
                    return True
        return False

    # Handle list[Type] syntax
    if type_str.startswith('list[') and type_str.endswith(']'):
        inner = type_str[5:-1].strip()
        # Check if the inner type belongs to another module
        type_module = get_type_module(inner)
        if type_module and type_module != current_module:
            return True
        return not is_primitive_type(inner)

    # For simple types, check if they belong to another module
    type_module = get_type_module(type_str)
    if type_module and type_module != current_module:
        return True

    return False


def extract_type_annotation(line: str) -> Tuple[str, str]:
    """Extract the type annotation from a field definition line."""
    # Pattern: field_name: TYPE = Field(...)
    match = re.search(r':\s*([^=]+?)\s*=\s*Field', line)
    if match:
        type_str = match.group(1).strip()
        return type_str, match.start(), match.end()
    return None, None, None


def quote_type_annotation(line: str, current_module: str) -> str:
    """Quote type annotation if it references types from other modules."""
    type_str, start, end = extract_type_annotation(line)
    if not type_str:
        return line

    if should_quote_type(type_str, current_module):
        # Quote the type annotation
        prefix = line[:start]
        suffix = line[end:]
        return f'{prefix}: "{type_str}" = Field{suffix}'

    return line


def fix_module_file(file_path: Path, module_name: str) -> int:
    """Fix forward references in a module file."""
    with open(file_path, 'r') as f:
        lines = f.readlines()

    fixed_lines = []
    changes = 0

    for line in lines:
        fixed_line = quote_type_annotation(line, module_name)
        if fixed_line != line:
            changes += 1
        fixed_lines.append(fixed_line)

    if changes > 0:
        with open(file_path, 'w') as f:
            f.writelines(fixed_lines)
        print(f"  ✓ Fixed {changes} forward references in {file_path.name}")
    else:
        print(f"  - No changes needed in {file_path.name}")

    return changes


def main():
    """Fix forward references in all telegram_api modules."""
    print("Fixing forward references in telegram_api modules...")
    print()

    base_dir = Path(__file__).resolve().parents[1] / "telegram_api"

    module_files = {
        'types': base_dir / 'types.py',
        'methods': base_dir / 'methods.py',
        'getting_updates': base_dir / 'getting_updates.py',
        'stickers': base_dir / 'stickers.py',
        'inline_mode': base_dir / 'inline_mode.py',
        'payments': base_dir / 'payments.py',
        'passport': base_dir / 'passport.py',
        'games': base_dir / 'games.py',
        'updating_messages': base_dir / 'updating_messages.py',
    }

    total_changes = 0
    for module_name, file_path in module_files.items():
        if file_path.exists():
            print(f"Processing {module_name}...")
            changes = fix_module_file(file_path, module_name)
            total_changes += changes
        else:
            print(f"  ⚠ File not found: {file_path}")

    print()
    print(f"✓ Total forward references fixed: {total_changes}")
    print()
    print("Now rebuild Python cache and run tests:")
    print("  find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null")
    print("  find . -name '*.pyc' -delete 2>/dev/null")
    print("  python -m pytest tests/test_types.py -v")


if __name__ == "__main__":
    main()
