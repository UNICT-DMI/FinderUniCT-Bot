"""
    /report command
"""
from telegram import Update
from telegram.ext import ContextTypes

async def report(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
        Called by the /report command
        Sends a report to the admin group

        Args:
            update: update event
            context: context passed by the handler
    """
    # post(update, context)
    print(update, context)

# Here is an example on how to log everyone's messages to a central location using MQTT.
# def post(topic: str, payload: str, retain: bool = False,
#          _client=establishBroker()):
#     """
#     Post msg to MQTT broker
#
#     :type _client: object
#     :type retain: bool
#     :param _client: Logging handler. By default, it is created by this module
#     :param retain: Retain topic on broker
#     :param topic: Project name
#     :param payload: Sensor Data
#     """
#     topic = str(f'{project}/{topic}')
#     payload = str(payload)
#     try:
#         _client.publish(topic=topic, payload=payload, qos=0, retain=retain)
#     except ValueError:
#         logger.warning(
#                 f"pub Failed because of wildcard: {str(topic)}=:={str(payload)}")
#         logger.warning(f"Attempting fix...")
#         try:
#             tame_t = topic.replace("+", "_")
#             tame_topic = tame_t.replace("#", "_")
#             tame_p = payload.replace("+", "_")
#             tame_payload = tame_p.replace("#", "_")
#             _client.publish(topic=str(tame_topic), payload=str(tame_payload),
#                             qos=1, retain=retain)
#             logger.debug("Fix successful, Sending data...")
#         except Exception as error:
#             logger.warning(f"Fix Failed. Bug report sent.")
#             _client.publish(f"{project}/error", str(error), qos=1, retain=True)
