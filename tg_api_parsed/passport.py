"""Telegram Bot API models.

Auto-generated from API documentation.
This module contains Passport.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

class EncryptedCredentials(BaseModel):
    """
    EncryptedCredentials type from Telegram Bot API.
    """

    data: str = Field(description="Base64-encoded encrypted JSON-serialized data with unique user's payload, data hashes and secrets required for EncryptedPassportElement decryption and authentication")
    hash: str = Field(description="Base64-encoded data hash for data authentication")
    secret: str = Field(description="Base64-encoded secret, encrypted with the bot's public RSA key, required for data decryption")
class EncryptedPassportElement(BaseModel):
    """
    EncryptedPassportElement type from Telegram Bot API.
    """

    type: str = Field(description="Element type. One of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”, “phone_number”, “email”.")
    data: None | str = Field(default=None, description="Optional . Base64-encoded encrypted Telegram Passport element data provided by the user; available only for “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport” and “address” types. Can be decrypted and verified using the accompanying EncryptedCredentials .")
    phone_number: None | str = Field(default=None, description="Optional . User's verified phone number; available only for “phone_number” type")
    email: None | str = Field(default=None, description="Optional . User's verified email address; available only for “email” type")
    files: "None | list[PassportFile]" = Field(default=None, description="Optional . Array of encrypted files with documents provided by the user; available only for “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials .")
    front_side: "None | PassportFile" = Field(default=None, description="Optional . Encrypted file with the front side of the document, provided by the user; available only for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials .")
    reverse_side: "None | PassportFile" = Field(default=None, description="Optional . Encrypted file with the reverse side of the document, provided by the user; available only for “driver_license” and “identity_card”. The file can be decrypted and verified using the accompanying EncryptedCredentials .")
    selfie: "None | PassportFile" = Field(default=None, description="Optional . Encrypted file with the selfie of the user holding a document, provided by the user; available if requested for “passport”, “driver_license”, “identity_card” and “internal_passport”. The file can be decrypted and verified using the accompanying EncryptedCredentials .")
    translation: "None | list[PassportFile]" = Field(default=None, description="Optional . Array of encrypted files with translated versions of documents provided by the user; available if requested for “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration” and “temporary_registration” types. Files can be decrypted and verified using the accompanying EncryptedCredentials .")
    hash: str = Field(description="Base64-encoded element hash for using in PassportElementErrorUnspecified")
class PassportData(BaseModel):
    """
    PassportData type from Telegram Bot API.
    """

    data: "list[EncryptedPassportElement]" = Field(description="Array with information about documents and other Telegram Passport elements that was shared with the bot")
    credentials: "EncryptedCredentials" = Field(description="Encrypted credentials required to decrypt the data")
class PassportElementError(BaseModel):
    """
    PassportElementError type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be data")
    type: str = Field(description="The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”")
    field_name: str = Field(description="Name of the data field which has the error")
    data_hash: str = Field(description="Base64-encoded data hash")
    message: str = Field(description="Error message")
class PassportElementErrorDataField(BaseModel):
    """
    PassportElementErrorDataField type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be data")
    type: str = Field(description="The section of the user's Telegram Passport which has the error, one of “personal_details”, “passport”, “driver_license”, “identity_card”, “internal_passport”, “address”")
    field_name: str = Field(description="Name of the data field which has the error")
    data_hash: str = Field(description="Base64-encoded data hash")
    message: str = Field(description="Error message")
class PassportElementErrorFile(BaseModel):
    """
    PassportElementErrorFile type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be file")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hash: str = Field(description="Base64-encoded file hash")
    message: str = Field(description="Error message")
class PassportElementErrorFiles(BaseModel):
    """
    PassportElementErrorFiles type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be files")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hashes: list[str] = Field(description="List of base64-encoded file hashes")
    message: str = Field(description="Error message")
class PassportElementErrorFrontSide(BaseModel):
    """
    PassportElementErrorFrontSide type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be front_side")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the front side of the document")
    message: str = Field(description="Error message")
class PassportElementErrorReverseSide(BaseModel):
    """
    PassportElementErrorReverseSide type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be reverse_side")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “driver_license”, “identity_card”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the reverse side of the document")
    message: str = Field(description="Error message")
class PassportElementErrorSelfie(BaseModel):
    """
    PassportElementErrorSelfie type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be selfie")
    type: str = Field(description="The section of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”")
    file_hash: str = Field(description="Base64-encoded hash of the file with the selfie")
    message: str = Field(description="Error message")
class PassportElementErrorTranslationFile(BaseModel):
    """
    PassportElementErrorTranslationFile type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be translation_file")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hash: str = Field(description="Base64-encoded file hash")
    message: str = Field(description="Error message")
class PassportElementErrorTranslationFiles(BaseModel):
    """
    PassportElementErrorTranslationFiles type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be translation_files")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue, one of “passport”, “driver_license”, “identity_card”, “internal_passport”, “utility_bill”, “bank_statement”, “rental_agreement”, “passport_registration”, “temporary_registration”")
    file_hashes: list[str] = Field(description="List of base64-encoded file hashes")
    message: str = Field(description="Error message")
class PassportElementErrorUnspecified(BaseModel):
    """
    PassportElementErrorUnspecified type from Telegram Bot API.
    """

    source: str = Field(description="Error source, must be unspecified")
    type: str = Field(description="Type of element of the user's Telegram Passport which has the issue")
    element_hash: str = Field(description="Base64-encoded element hash")
    message: str = Field(description="Error message")
class PassportFile(BaseModel):
    """
    PassportFile type from Telegram Bot API.
    """

    file_id: str = Field(description="Identifier for this file, which can be used to download or reuse the file")
    file_unique_id: str = Field(description="Unique identifier for this file, which is supposed to be the same over time and for different bots. Can't be used to download or reuse the file.")
    file_size: int = Field(description="File size in bytes")
    file_date: int = Field(description="Unix time when the file was uploaded")
class setPassportDataErrors(BaseModel):
    """
    setPassportDataErrors method from Telegram Bot API.
    """

    user_id: int = Field(description="User identifier")
    errors: "list[PassportElementError]" = Field(description="A JSON-serialized array describing the errors")
