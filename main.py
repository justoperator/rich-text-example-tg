import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, InputRichMessage
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    html = """
<h1>Lorem Ipsum Dolor</h1>
<p>Lorem ipsum dolor sit amet, <b>consectetur adipiscing elit</b>. Sed do <i>eiusmod tempor incididunt</i> ut labore et dolore magna aliqua. <u>Ut enim ad minim veniam</u>, quis nostrud exercitation ullamco.</p>

<h2>Feature List</h2>
<ul>
<li>Duis aute irure dolor in reprehenderit</li>
<li>Excepteur sint occaecat cupidatat non proident</li>
<li>Sunt in culpa qui officia deserunt mollit anim</li>
</ul>

<h2>Task Checklist</h2>
<ul>
<li><input type="checkbox" checked disabled/> Curabitur pretium tincidunt lacus</li>
<li><input type="checkbox" disabled/> Nulla gravida orci a odio</li>
<li><input type="checkbox" disabled/> Aenean sollicitudin lorem quis bibendum</li>
</ul>

<h2>Numbered List</h2>
<ol>
<li>Vestibulum ante ipsum primis in faucibus</li>
<li>Orci luctus et ultrices posuere cubilia curae</li>
<li>Class aptent taciti sociosqu ad litora torquent</li>
</ol>

<h2>Quote</h2>
<blockquote>Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium.Marcus Tullius Cicero</blockquote>

<h2>Table</h2>
<table bordered striped>
<caption>Sample Data</caption>
<tr><th>Name</th><th>Value</th></tr>
<tr><td>Lorem</td><td>Ipsum</td></tr>
<tr><td>Dolor</td><td>Sit Amet</td></tr>
</table>

<hr/>

<h2>Slideshow</h2>
<tg-slideshow>
<img src="https://picsum.photos/800/600"/>
<img src="https://picsum.photos/800/601"/>
<img src="https://picsum.photos/800/602"/>
</tg-slideshow>

<h2>Collage</h2>
<tg-collage>
<img src="https://picsum.photos/800/610"/>
<img src="https://picsum.photos/800/611"/>
<img src="https://picsum.photos/800/612"/>
</tg-collage>

<details>
<summary>Expandable Block</summary>
<p>Curabitur blandit tempus porttitor. Maecenas faucibus mollis interdum. Donec sed odio dui.</p>
</details>

<footer>Lorem Ipsum Generator &mdash; 2026</footer>
"""

    await message.answer_rich(
        rich_message=InputRichMessage(html=html)
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
