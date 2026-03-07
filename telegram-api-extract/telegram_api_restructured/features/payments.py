from __future__ import annotations

"""Telegram Bot API - Payments."""

from pydantic import BaseModel, Field
from ..core import User, Chat, Message
from ..types import Update

class AffiliateInfo(BaseModel):
    """
    AffiliateInfo type from Telegram Bot API.
    """

    affiliate_user: None | User = Field(default=None, description="Optional . The bot or the user that received an affiliate commission if it was received by a bot or a user")
    affiliate_chat: None | Chat = Field(default=None, description="Optional . The chat that received an affiliate commission if it was received by a chat")
    commission_per_mille: int = Field(description="The number of Telegram Stars received by the affiliate for each 1000 Telegram Stars received by the bot from referred users")
    amount: int = Field(description="Integer amount of Telegram Stars received by the affiliate from the transaction, rounded to 0; can be negative for refunds")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars received by the affiliate; from -999999999 to 999999999; can be negative for refunds")
class Invoice(BaseModel):
    """
    Invoice type from Telegram Bot API.
    """

    title: str = Field(description="Product name")
    description: str = Field(description="Product description")
    start_parameter: str = Field(description="Unique bot deep-linking parameter that can be used to generate this invoice")
    currency: str = Field(description="Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram Stars")
    total_amount: int = Field(description="Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
class LabeledPrice(BaseModel):
    """
    LabeledPrice type from Telegram Bot API.
    """

    label: str = Field(description="Portion label")
    amount: int = Field(description="Price of the product in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
class OrderInfo(BaseModel):
    """
    OrderInfo type from Telegram Bot API.
    """

    name: None | str = Field(default=None, description="Optional . User name")
    phone_number: None | str = Field(default=None, description="Optional . User's phone number")
    email: None | str = Field(default=None, description="Optional . User email")
    shipping_address: None | ShippingAddress = Field(default=None, description="Optional . User shipping address")
class PaidMediaPurchased(BaseModel):
    """
    PaidMediaPurchased type from Telegram Bot API.
    """

    from_: User = Field(description="User who purchased the media")
    paid_media_payload: str = Field(description="Bot-specified paid media payload")
class PreCheckoutQuery(BaseModel):
    """
    PreCheckoutQuery type from Telegram Bot API.
    """

    id: str = Field(description="Unique query identifier")
    from_: User = Field(description="User who sent the query")
    currency: str = Field(description="Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram Stars")
    total_amount: int = Field(description="Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
    invoice_payload: str = Field(description="Bot-specified invoice payload")
    shipping_option_id: None | str = Field(default=None, description="Optional . Identifier of the shipping option chosen by the user")
    order_info: None | OrderInfo = Field(default=None, description="Optional . Order information provided by the user")
class RefundedPayment(BaseModel):
    """
    RefundedPayment type from Telegram Bot API.
    """

    currency: str = Field(description="Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram Stars . Currently, always “XTR”")
    total_amount: int = Field(description="Total refunded price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 , total_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
    invoice_payload: str = Field(description="Bot-specified invoice payload")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier")
    provider_payment_charge_id: None | str = Field(default=None, description="Optional . Provider payment identifier")
class RevenueWithdrawalState(BaseModel):
    """
    RevenueWithdrawalState type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “pending”")
class RevenueWithdrawalStateFailed(BaseModel):
    """
    RevenueWithdrawalStateFailed type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “failed”")
class RevenueWithdrawalStatePending(BaseModel):
    """
    RevenueWithdrawalStatePending type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “pending”")
class RevenueWithdrawalStateSucceeded(BaseModel):
    """
    RevenueWithdrawalStateSucceeded type from Telegram Bot API.
    """

    type: str = Field(description="Type of the state, always “succeeded”")
    date: int = Field(description="Date the withdrawal was completed in Unix time")
    url: str = Field(description="An HTTPS URL that can be used to see transaction details")
class ShippingAddress(BaseModel):
    """
    ShippingAddress type from Telegram Bot API.
    """

    country_code: str = Field(description="Two-letter ISO 3166-1 alpha-2 country code")
    state: str = Field(description="State, if applicable")
    city: str = Field(description="City")
    street_line1: str = Field(description="First line for the address")
    street_line2: str = Field(description="Second line for the address")
    post_code: str = Field(description="Address post code")
class ShippingOption(BaseModel):
    """
    ShippingOption type from Telegram Bot API.
    """

    id: str = Field(description="Shipping option identifier")
    title: str = Field(description="Option title")
    prices: list[LabeledPrice] = Field(description="List of price portions")
class ShippingQuery(BaseModel):
    """
    ShippingQuery type from Telegram Bot API.
    """

    id: str = Field(description="Unique query identifier")
    from_: User = Field(description="User who sent the query")
    invoice_payload: str = Field(description="Bot-specified invoice payload")
    shipping_address: ShippingAddress = Field(description="User specified shipping address")
class StarTransaction(BaseModel):
    """
    StarTransaction type from Telegram Bot API.
    """

    id: str = Field(description="Unique identifier of the transaction. Coincides with the identifier of the original transaction for refund transactions. Coincides with SuccessfulPayment.telegram_payment_charge_id for successful incoming payments from users.")
    amount: int = Field(description="Integer amount of Telegram Stars transferred by the transaction")
    nanostar_amount: None | int = Field(default=None, description="Optional . The number of 1/1000000000 shares of Telegram Stars transferred by the transaction; from 0 to 999999999")
    date: int = Field(description="Date the transaction was created in Unix time")
    source: None | TransactionPartner = Field(default=None, description="Optional . Source of an incoming transaction (e.g., a user purchasing goods or services, Fragment refunding a failed withdrawal). Only for incoming transactions")
    receiver: None | TransactionPartner = Field(default=None, description="Optional . Receiver of an outgoing transaction (e.g., a user for a purchase refund, Fragment for a withdrawal). Only for outgoing transactions")
class StarTransactions(BaseModel):
    """
    StarTransactions type from Telegram Bot API.
    """

    transactions: list[StarTransaction] = Field(description="The list of transactions")
class SuccessfulPayment(BaseModel):
    """
    SuccessfulPayment type from Telegram Bot API.
    """

    currency: str = Field(description="Three-letter ISO 4217 currency code, or “XTR” for payments in Telegram Stars")
    total_amount: int = Field(description="Total price in the smallest units of the currency (integer, not float/double). For example, for a price of US$ 1.45 pass amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies).")
    invoice_payload: str = Field(description="Bot-specified invoice payload")
    subscription_expiration_date: None | int = Field(default=None, description="Optional . Expiration date of the subscription, in Unix time; for recurring payments only")
    is_recurring: None | bool = Field(default=None, description="Optional . True , if the payment is a recurring payment for a subscription")
    is_first_recurring: None | bool = Field(default=None, description="Optional . True , if the payment is the first payment for a subscription")
    shipping_option_id: None | str = Field(default=None, description="Optional . Identifier of the shipping option chosen by the user")
    order_info: None | OrderInfo = Field(default=None, description="Optional . Order information provided by the user")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier")
    provider_payment_charge_id: str = Field(description="Provider payment identifier")
class TransactionPartner(BaseModel):
    """
    TransactionPartner type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “user”")
    transaction_type: str = Field(description="Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts")
    user: User = Field(description="Information about the user")
    affiliate: None | AffiliateInfo = Field(default=None, description="Optional . Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.")
    invoice_payload: None | str = Field(default=None, description="Optional . Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.")
    subscription_period: None | int = Field(default=None, description="Optional . The duration of the paid subscription. Can be available only for “invoice_payment” transactions.")
    paid_media: None | list[PaidMedia] = Field(default=None, description="Optional . Information about the paid media bought by the user; for “paid_media_payment” transactions only")
    paid_media_payload: None | str = Field(default=None, description="Optional . Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the user by the bot; for “gift_purchase” transactions only")
    premium_subscription_duration: None | int = Field(default=None, description="Optional . Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only")
class TransactionPartnerAffiliateProgram(BaseModel):
    """
    TransactionPartnerAffiliateProgram type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “affiliate_program”")
    sponsor_user: None | User = Field(default=None, description="Optional . Information about the bot that sponsored the affiliate program")
    commission_per_mille: int = Field(description="The number of Telegram Stars received by the bot for each 1000 Telegram Stars received by the affiliate program sponsor from referred users")
class TransactionPartnerChat(BaseModel):
    """
    TransactionPartnerChat type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “chat”")
    chat: Chat = Field(description="Information about the chat")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the chat by the bot")
class TransactionPartnerFragment(BaseModel):
    """
    TransactionPartnerFragment type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “fragment”")
    withdrawal_state: None | RevenueWithdrawalState = Field(default=None, description="Optional . State of the transaction if the transaction is outgoing")
class TransactionPartnerOther(BaseModel):
    """
    TransactionPartnerOther type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “other”")
class TransactionPartnerTelegramAds(BaseModel):
    """
    TransactionPartnerTelegramAds type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “telegram_ads”")
class TransactionPartnerTelegramApi(BaseModel):
    """
    TransactionPartnerTelegramApi type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “telegram_api”")
    request_count: int = Field(description="The number of successful requests that exceeded regular limits and were therefore billed")
class TransactionPartnerUser(BaseModel):
    """
    TransactionPartnerUser type from Telegram Bot API.
    """

    type: str = Field(description="Type of the transaction partner, always “user”")
    transaction_type: str = Field(description="Type of the transaction, currently one of “invoice_payment” for payments via invoices, “paid_media_payment” for payments for paid media, “gift_purchase” for gifts sent by the bot, “premium_purchase” for Telegram Premium subscriptions gifted by the bot, “business_account_transfer” for direct transfers from managed business accounts")
    user: User = Field(description="Information about the user")
    affiliate: None | AffiliateInfo = Field(default=None, description="Optional . Information about the affiliate that received a commission via this transaction. Can be available only for “invoice_payment” and “paid_media_payment” transactions.")
    invoice_payload: None | str = Field(default=None, description="Optional . Bot-specified invoice payload. Can be available only for “invoice_payment” transactions.")
    subscription_period: None | int = Field(default=None, description="Optional . The duration of the paid subscription. Can be available only for “invoice_payment” transactions.")
    paid_media: None | list[PaidMedia] = Field(default=None, description="Optional . Information about the paid media bought by the user; for “paid_media_payment” transactions only")
    paid_media_payload: None | str = Field(default=None, description="Optional . Bot-specified paid media payload. Can be available only for “paid_media_payment” transactions.")
    gift: None | Gift = Field(default=None, description="Optional . The gift sent to the user by the bot; for “gift_purchase” transactions only")
    premium_subscription_duration: None | int = Field(default=None, description="Optional . Number of months the gifted Telegram Premium subscription will be active for; for “premium_purchase” transactions only")
class answerPreCheckoutQuery(BaseModel):
    """
    answerPreCheckoutQuery method from Telegram Bot API.
    """

    pre_checkout_query_id: str = Field(description="Unique identifier for the query to be answered")
    ok: bool = Field(description="Specify True if everything is alright (goods are available, etc.) and the bot is ready to proceed with the order. Use False if there are any problems.")
    error_message: None | str = Field(default=None, description="Required if ok is False . Error message in human readable form that explains the reason for failure to proceed with the checkout (e.g. \"Sorry, somebody just bought the last of our amazing black T-shirts while you were busy filling out your payment details. Please choose a different color or garment!\"). Telegram will display this message to the user.")
class answerShippingQuery(BaseModel):
    """
    answerShippingQuery method from Telegram Bot API.
    """

    shipping_query_id: str = Field(description="Unique identifier for the query to be answered")
    ok: bool = Field(description="Pass True if delivery to the specified address is possible and False if there are any problems (for example, if delivery to the specified address is not possible)")
    shipping_options: None | list[ShippingOption] = Field(default=None, description="Required if ok is True . A JSON-serialized array of available shipping options.")
    error_message: None | str = Field(default=None, description="Required if ok is False . Error message in human readable form that explains why it is impossible to complete the order (e.g. “Sorry, delivery to your desired address is unavailable”). Telegram will display this message to the user.")
class createInvoiceLink(BaseModel):
    """
    createInvoiceLink method from Telegram Bot API.
    """

    business_connection_id: None | str = Field(default=None, description="Unique identifier of the business connection on behalf of which the link will be created. For payments in Telegram Stars only.")
    title: str = Field(description="Product name, 1-32 characters")
    description: str = Field(description="Product description, 1-255 characters")
    payload: str = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: None | str = Field(default=None, description="Payment provider token, obtained via @BotFather . Pass an empty string for payments in Telegram Stars .")
    currency: str = Field(description="Three-letter ISO 4217 currency code, see more on currencies . Pass “XTR” for payments in Telegram Stars .")
    prices: list[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars .")
    subscription_period: None | int = Field(default=None, description="The number of seconds the subscription will be active for before the next payment. The currency must be set to “XTR” (Telegram Stars) if the parameter is used. Currently, it must always be 2592000 (30 days) if specified. Any number of subscriptions can be active for a given bot at the same time, including multiple concurrent subscriptions from the same user. Subscription price must no exceed 10000 Telegram Stars.")
    max_tip_amount: None | int = Field(default=None, description="The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars .")
    suggested_tip_amounts: None | list[int] = Field(default=None, description="A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount .")
    provider_data: None | str = Field(default=None, description="JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.")
    photo_url: None | str = Field(default=None, description="URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service.")
    photo_size: None | int = Field(default=None, description="Photo size in bytes")
    photo_width: None | int = Field(default=None, description="Photo width")
    photo_height: None | int = Field(default=None, description="Photo height")
    need_name: None | bool = Field(default=None, description="Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars .")
    need_phone_number: None | bool = Field(default=None, description="Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars .")
    need_email: None | bool = Field(default=None, description="Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars .")
    need_shipping_address: None | bool = Field(default=None, description="Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars .")
    send_phone_number_to_provider: None | bool = Field(default=None, description="Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars .")
    send_email_to_provider: None | bool = Field(default=None, description="Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars .")
    is_flexible: None | bool = Field(default=None, description="Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars .")
class editUserStarSubscription(BaseModel):
    """
    editUserStarSubscription method from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the user whose subscription will be edited")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier for the subscription")
    is_canceled: bool = Field(description="Pass True to cancel extension of the user subscription; the subscription must be active up to the end of the current subscription period. Pass False to allow the user to re-enable a subscription that was previously canceled by the bot.")
class getMyStarBalance(BaseModel):
    """
    getMyStarBalance method from Telegram Bot API.
    """

    offset: None | int = Field(default=None, description="Number of transactions to skip in the response")
    limit: None | int = Field(default=None, description="The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class getStarTransactions(BaseModel):
    """
    getStarTransactions method from Telegram Bot API.
    """

    offset: None | int = Field(default=None, description="Number of transactions to skip in the response")
    limit: None | int = Field(default=None, description="The maximum number of transactions to be retrieved. Values between 1-100 are accepted. Defaults to 100.")
class refundStarPayment(BaseModel):
    """
    refundStarPayment method from Telegram Bot API.
    """

    user_id: int = Field(description="Identifier of the user whose payment will be refunded")
    telegram_payment_charge_id: str = Field(description="Telegram payment identifier")
class sendInvoice(BaseModel):
    """
    sendInvoice method from Telegram Bot API.
    """

    chat_id: int | str = Field(description="Unique identifier for the target chat or username of the target channel (in the format @channelusername )")
    message_thread_id: None | int = Field(default=None, description="Unique identifier for the target message thread (topic) of a forum; for forum supergroups and private chats of bots with forum topic mode enabled only")
    direct_messages_topic_id: None | int = Field(default=None, description="Identifier of the direct messages topic to which the message will be sent; required if the message is sent to a direct messages chat")
    title: str = Field(description="Product name, 1-32 characters")
    description: str = Field(description="Product description, 1-255 characters")
    payload: str = Field(description="Bot-defined invoice payload, 1-128 bytes. This will not be displayed to the user, use it for your internal processes.")
    provider_token: None | str = Field(default=None, description="Payment provider token, obtained via @BotFather . Pass an empty string for payments in Telegram Stars .")
    currency: str = Field(description="Three-letter ISO 4217 currency code, see more on currencies . Pass “XTR” for payments in Telegram Stars .")
    prices: list[LabeledPrice] = Field(description="Price breakdown, a JSON-serialized list of components (e.g. product price, tax, discount, delivery cost, delivery tax, bonus, etc.). Must contain exactly one item for payments in Telegram Stars .")
    max_tip_amount: None | int = Field(default=None, description="The maximum accepted amount for tips in the smallest units of the currency (integer, not float/double). For example, for a maximum tip of US$ 1.45 pass max_tip_amount = 145 . See the exp parameter in currencies.json , it shows the number of digits past the decimal point for each currency (2 for the majority of currencies). Defaults to 0. Not supported for payments in Telegram Stars .")
    suggested_tip_amounts: None | list[int] = Field(default=None, description="A JSON-serialized array of suggested amounts of tips in the smallest units of the currency (integer, not float/double). At most 4 suggested tip amounts can be specified. The suggested tip amounts must be positive, passed in a strictly increased order and must not exceed max_tip_amount .")
    start_parameter: None | str = Field(default=None, description="Unique deep-linking parameter. If left empty, forwarded copies of the sent message will have a Pay button, allowing multiple users to pay directly from the forwarded message, using the same invoice. If non-empty, forwarded copies of the sent message will have a URL button with a deep link to the bot (instead of a Pay button), with the value used as the start parameter")
    provider_data: None | str = Field(default=None, description="JSON-serialized data about the invoice, which will be shared with the payment provider. A detailed description of required fields should be provided by the payment provider.")
    photo_url: None | str = Field(default=None, description="URL of the product photo for the invoice. Can be a photo of the goods or a marketing image for a service. People like it better when they see what they are paying for.")
    photo_size: None | int = Field(default=None, description="Photo size in bytes")
    photo_width: None | int = Field(default=None, description="Photo width")
    photo_height: None | int = Field(default=None, description="Photo height")
    need_name: None | bool = Field(default=None, description="Pass True if you require the user's full name to complete the order. Ignored for payments in Telegram Stars .")
    need_phone_number: None | bool = Field(default=None, description="Pass True if you require the user's phone number to complete the order. Ignored for payments in Telegram Stars .")
    need_email: None | bool = Field(default=None, description="Pass True if you require the user's email address to complete the order. Ignored for payments in Telegram Stars .")
    need_shipping_address: None | bool = Field(default=None, description="Pass True if you require the user's shipping address to complete the order. Ignored for payments in Telegram Stars .")
    send_phone_number_to_provider: None | bool = Field(default=None, description="Pass True if the user's phone number should be sent to the provider. Ignored for payments in Telegram Stars .")
    send_email_to_provider: None | bool = Field(default=None, description="Pass True if the user's email address should be sent to the provider. Ignored for payments in Telegram Stars .")
    is_flexible: None | bool = Field(default=None, description="Pass True if the final price depends on the shipping method. Ignored for payments in Telegram Stars .")
    disable_notification: None | bool = Field(default=None, description="Sends the message silently . Users will receive a notification with no sound.")
    protect_content: None | bool = Field(default=None, description="Protects the contents of the sent message from forwarding and saving")
    allow_paid_broadcast: None | bool = Field(default=None, description="Pass True to allow up to 1000 messages per second, ignoring broadcasting limits for a fee of 0.1 Telegram Stars per message. The relevant Stars will be withdrawn from the bot's balance")
    message_effect_id: None | str = Field(default=None, description="Unique identifier of the message effect to be added to the message; for private chats only")
    suggested_post_parameters: None | SuggestedPostParameters = Field(default=None, description="A JSON-serialized object containing the parameters of the suggested post to send; for direct messages chats only. If the message is sent as a reply to another suggested post, then that suggested post is automatically declined.")
    reply_parameters: None | ReplyParameters = Field(default=None, description="Description of the message to reply to")
    reply_markup: None | InlineKeyboardMarkup = Field(default=None, description="A JSON-serialized object for an inline keyboard . If empty, one 'Pay total price ' button will be shown. If not empty, the first button must be a Pay button.")
