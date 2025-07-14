import requests

ALERTS = [
    {
        "id": "1",
        "on_click": [
            {
                "type": "show_content",
                "content": {
                    "type": "html",
                    "title": "",
                    "data": '<div style="max-width: 600px; margin: 0 auto; padding: 1rem; font-family: Arial, sans-serif; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><div style="text-align: center; margin-bottom: 0.75rem;"><div style="font-size: 2.5rem; color: #f39c12; margin-bottom: 0.5rem;">🔧</div><h2 style="color: #f39c12; margin: 0 0 0.5rem 0;">Scheduled Maintenance</h2></div><div style="color: #333; line-height: 1.4; margin-bottom: 0.75rem;"><p>Our services will be unavailable due to scheduled maintenance from 12:00 AM to 4:00 AM.</p><p>During this time, all services will be temporarily offline while we perform necessary system updates.</p></div><div style="background: #f8f9fa; padding: 0.75rem; border-radius: 6px; text-align: center;"><p style="margin: 0.25rem 0;">⏰ Maintenance Window:</p><p style="color: #f39c12; font-weight: bold; margin: 0;">12:00 AM - 4:00 AM</p></div><p style="color: #666; font-size: 0.9rem; margin: 0.75rem 0 0 0; text-align: center;">We apologize for any inconvenience and thank you for your patience.</p></div>',
                    "actions": [{"label": "Close", "style": "text", "on_click": []}],
                },
                "mark_as_read": False,
                "hide_behavior": "never",
                "barrier_dismissible": False,
            }
        ],
    },
    {
        "id": "2",
        "on_click": [
            {
                "type": "show_dialog",
                "content": {
                    "type": "html",
                    "title": "",
                    "data": '<div style="max-width: 600px; margin: 0 auto; padding: 1rem; font-family: Arial, sans-serif; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><div style="text-align: center; margin-bottom: 0.75rem;"><div style="font-size: 2.5rem; color: #dc3545; margin-bottom: 0.5rem;">⚠️</div><h2 style="color: #dc3545; margin: 0 0 0.5rem 0;">Account Suspended</h2></div><div style="color: #333; line-height: 1.4; margin-bottom: 0.75rem;"><p>Your account has been temporarily suspended due to suspicious activity detected in your account.</p><p>This suspension is necessary to protect your account and our community. Please contact our support team to resolve this issue.</p></div><div style="background: #f8f9fa; padding: 0.75rem; border-radius: 6px; text-align: center;"><p style="margin: 0.25rem 0;">📧 Contact Support:</p><a href="mailto:support@ezyli.com" style="color: #007bff; text-decoration: none; font-weight: bold;">support@ezyli.com</a></div><p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0 0; text-align: center;">We appreciate your understanding and cooperation.</p></div>',
                    "actions": [
                        {"label": "Close", "style": "text", "on_click": []},
                        {
                            "label": "Close App",
                            "style": "outlined",
                            "on_click": [{"type": "close_app"}],
                        },
                    ],
                },
                "mark_as_read": False,
                "hide_behavior": "never",
                "barrier_dismissible": False,
            },
        ],
    },
    {
        "id": "2",
        "on_click": [
            {
                "type": "show_dialog",
                "content": {
                    "type": "html",
                    "title": "",
                    "data": '<div style="max-width: 600px; margin: 0 auto; padding: 1rem; font-family: Arial, sans-serif; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><div style="text-align: center; margin-bottom: 0.75rem;"><div style="font-size: 2.5rem; color: #dc3545; margin-bottom: 0.5rem;">⚠️</div><h2 style="color: #dc3545; margin: 0 0 0.5rem 0;">Account Suspended</h2></div><div style="color: #333; line-height: 1.4; margin-bottom: 0.75rem;"><p>Your account has been temporarily suspended due to suspicious activity detected in your account.</p><p>This suspension is necessary to protect your account and our community. Please contact our support team to resolve this issue.</p></div><div style="background: #f8f9fa; padding: 0.75rem; border-radius: 6px; text-align: center;"><p style="margin: 0.25rem 0;">📧 Contact Support:</p><a href="mailto:support@ezyli.com" style="color: #007bff; text-decoration: none; font-weight: bold;">support@ezyli.com</a></div><p style="color: #666; font-size: 0.9rem; margin: 0.5rem 0 0 0; text-align: center;">We appreciate your understanding and cooperation.</p></div>',
                    "actions": [
                        {
                            "label": "Close",
                            "style": "text",
                            "on_click": [],
                        },
                        {
                            "label": "Continue",
                            "style": "outlined",
                            "on_click": [
                                {
                                    "type": "show_content",
                                    "content": {
                                        "type": "html",
                                        "title": "",
                                        "data": '<div style="max-width: 600px; margin: 0 auto; padding: 1rem; font-family: Arial, sans-serif; background: #fff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);"><div style="text-align: center; margin-bottom: 0.75rem;"><div style="font-size: 2.5rem; color: #f39c12; margin-bottom: 0.5rem;">🔧</div><h2 style="color: #f39c12; margin: 0 0 0.5rem 0;">Scheduled Maintenance</h2></div><div style="color: #333; line-height: 1.4; margin-bottom: 0.75rem;"><p>Our services will be unavailable due to scheduled maintenance from 12:00 AM to 4:00 AM.</p><p>During this time, all services will be temporarily offline while we perform necessary system updates.</p></div><div style="background: #f8f9fa; padding: 0.75rem; border-radius: 6px; text-align: center;"><p style="margin: 0.25rem 0;">⏰ Maintenance Window:</p><p style="color: #f39c12; font-weight: bold; margin: 0;">12:00 AM - 4:00 AM</p></div><p style="color: #666; font-size: 0.9rem; margin: 0.75rem 0 0 0; text-align: center;">We apologize for any inconvenience and thank you for your patience.</p></div>',
                                        "actions": [
                                            {
                                                "label": "Close",
                                                "style": "text",
                                                "on_click": [],
                                            }
                                        ],
                                    },
                                    "mark_as_read": False,
                                    "hide_behavior": "never",
                                    "barrier_dismissible": False,
                                },
                            ],
                        },
                    ],
                },
                "mark_as_read": False,
                "hide_behavior": "never",
                "barrier_dismissible": False,
            },
        ],
    },
]
data = {
    "channel": "CLIENT_13",
    "event": "new_alert",
    "data": ALERTS[0],
}

url = "http://57.128.166.240/trip-order/fake_ws"

response = requests.post(url=url, json=data)
print(response.status_code)
