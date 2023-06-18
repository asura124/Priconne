from discord.ui import View
from discord import ui
import discord
from typing import Optional, List

class ButtonMenu(View):
    def __init__(self,pages:list,timeout:float,user:Optional[discord.Member]=None) -> None:
        super().__init__(timeout=timeout)
        self.current_page = 0
        self.pages = pages
        self.user = user
        self.length = len(self.pages) - 1
        self.children[0].disabled = True
        self.children[1].disabled = True
        if(self.length==0):
            self.children[-1].disabled = True
            self.children[-2].disabled = True

    async def update(self,page:int):
        self.current_page = page
        if(page==0):
            self.children[0].disabled = True
            self.children[1].disabled = True
            self.children[-1].disabled = False
            self.children[-2].disabled = False
        elif(page==self.length):
            self.children[0].disabled = False
            self.children[1].disabled = False
            self.children[-1].disabled = True
            self.children[-2].disabled = True
        else:
            self.children[0].disabled = False
            self.children[1].disabled = False
            self.children[-1].disabled = False
            self.children[-2].disabled = False

    async def getPage(self,page):
        return [page]
    
    async def showPage(self,page:int,interaction):
        await self.update(page)
        embeds = await self.getPage(self.pages[page])
        await interaction.response.edit_message(embeds = embeds,view=self)

    @ui.button(emoji = "⏮")
    async def first_page(self,interaction,button):
        await self.showPage(0,interaction)
    
    @ui.button(emoji = "⏪")
    async def before_page(self,interaction,button):
        await self.showPage(self.current_page-1,interaction)

    @ui.button(emoji = "🛑")
    async def stop_page(self,interaction,button):
        for i in self.children:
            i.disabled = True
        await interaction.response.edit_message(view=self)
        self.stop()

    @ui.button(emoji = "⏩")
    async def next_page(self,interaction,button):
        await self.showPage(self.current_page+1,interaction)

    @ui.button(emoji = "⏭")
    async def last_page(self,interaction,button):
        await self.showPage(self.length,interaction)

    async def interaction_check(self,interaction):
        if(self.user):
            if(interaction.user != self.user):
                await interaction.response.send_message("This command is not for you!")
                return False
        return True