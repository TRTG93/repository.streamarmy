from resources.libs.modules.scrapers import soccerstreamsfrom resources.libs.modules.scrapers import livetvfrom resources.libs.modules.scrapers import tvschedfrom resources.libs.modules.scrapers import iptvfrom resources.libs.modules.scrapers import trendingtvfrom resources.libs.modules.scrapers import mamafrom resources.libs.modules.scrapers import disneyfrom resources.libs.modules.scrapers import cinemafrom resources.libs.modules.scrapers import threedfrom resources.libs.modules.scrapers import multifrom resources.libs.modules.scrapers import threetwoonefrom resources.libs.modules.scrapers import newmoviesfrom resources.libs.modules.scrapers import youtubefrom resources.libs.modules.scrapers import cctvfrom resources.libs.modules.scrapers import replaysfrom resources.libs.modules.scrapers import docsfrom resources.libs.modules.scrapers import docsthreedfrom resources.libs.modules.scrapers import radiofrom resources.libs.modules.scrapers import audiobooksfrom resources.libs.modules.scrapers import vrpornfrom resources.libs.modules.scrapers import pornhdfrom resources.libs.modules.scrapers import porncomfrom resources.libs.modules.scrapers import musicvidsfrom resources.libs.modules.scrapers import pawpatrolfrom resources.libs.modules.scrapers import transfersfrom resources.libs.modules.scrapers import epornerfrom resources.libs.modules.scrapers import fmoviesfrom resources.libs.modules.scrapers import tvboxdef getscraper(mode,url,name,iconimage,fanart):    if mode==12:soccerstreams.SCRAPE_SOCCERSTREAMS()    elif mode==13:soccerstreams.SCRAPE_SOCCERSTREAMS_GET_LINKS(url,iconimage)    elif mode==14:livetv.SCRAPE_FILMON_CATS()    elif mode==15:livetv.SCRAPE_FILMON_CHANS(url)    elif mode==16:tvsched.TV_SCHED()    elif mode==17:tvsched.TV_SCHED_CONTENT(url)    elif mode==18:tvsched.TV_SCHED_CONTENT_GRAB(url,iconimage,fanart)    elif mode==19:tvsched.TV_SCHED_CONTENT_GRAB_LINKS(url,iconimage,fanart)    elif mode==20:tvsched.TV_SCHED_CONTENT_GRAB_LINKS_PLAY(url,iconimage,fanart)    elif mode==21:iptv.SCRAPE_IPTV_CONTENT()    elif mode==22:iptv.SCRAPE_IPTV_PLAY(url)    elif mode==23:trendingtv.TRENDING_TV()    elif mode==24:mama.SCRAPE_SPORTSMAMA_GAMES(url)    elif mode==25:mama.SCRAPE_SPORTSMAMA_CHANS(name,url,iconimage)    elif mode==26:tvsched.TV_SEARCH()    elif mode==27:disney.SCRAPE_DISNEY_FILMS()    elif mode==28:disney.SCRAPE_DISNEY_LINKS(url)    elif mode==29:cinema.SCRAPE_123MOVIES(url)    elif mode==30:cinema.SCRAPE_123MOVIES_LINKS(url)    elif mode==31:cinema.SCRAPE_123MOVIES_PLAY(name,url,iconimage)    elif mode==32:threed.SCRAPE_3D_CONTENT(url)    elif mode==33:threed.SCRAPE_3D_PLAY(url,iconimage,fanart)    elif mode==34:multi.MULTI_SEARCH_SCRAPERS(url)    elif mode==35:threetwoone.SCRAPE_321MOVIES_LINKS(url)    elif mode==36:newmovies.SCRAPE_NEWMOVIESONLINE_LINKS(url)    elif mode==37:fmovies.SCRAPE_FMOVIES_CATS(url)    elif mode==38:fmovies.SCRAPE_FMOVIES_CONTENT(url)    elif mode==39:fmovies.SCRAPE_FMOVIES_LINKS(name,url,iconimage)    elif mode==40:fmovies.SCRAPE_FMOVIES_YEARS(url)    elif mode==42:youtube.YOUTUBE_PLAYLIST(url)    elif mode==43:youtube.YOUTUBE_PLAYLIST_PLAY(url)    elif mode==44:youtube.YOUTUBE_LIVE(url)    elif mode==45:youtube.SCRAPE_YOUTUBE_PLAY_LINK(name,url)    elif mode==46:cctv.SCRAPE_WEBCAM_CATS()    elif mode==47:cctv.SCRAPE_WEBCAM_LINKS(url)    elif mode==48:cctv.SCRAPE_WEBCAM_PLAYLINKS(name,url,iconimage)    elif mode==49:replays.SCRAPE_FULLHIGH(url)    elif mode==50:replays.SCRAPE_FULLHIGH_GET(url,iconimage,fanart)    elif mode==51:replays.SCRAPE_FULLHIGH_PLAY(url,name,iconimage)    elif mode==52:docs.SCRAPE_DOCS_CATS(url)    elif mode==53:docs.SCRAPE_DOCS_CONTENT(name,url,iconimage)    elif mode==54:docsthreed.SCRAPE_3D_DOCS(url)    elif mode==55:docsthreed.SCRAPE_3D_DOCS_LINKS(name,url,iconimage)    elif mode==56:radio.SCRAPE_RADIO_COUNTRYS()    elif mode==57:radio.SCRAPE_RADIO_LINKS(url)    elif mode==58:radio.PLAYRADIO(name,url,iconimage)    elif mode==59:audiobooks.SCRAPE_AUDIOBOOKS_CATS()    elif mode==60:audiobooks.SCRAPE_AUDIOBOOKS_CONTENT(url)    elif mode==61:audiobooks.SCRAPE_AUDIOBOOKS_LINKS(name,url,iconimage)    elif mode==62:vrporn.SCRAPE_VR_CATS()    elif mode==63:vrporn.SCRAPE_VR_VIDS(url)    elif mode==64:vrporn.PLAY_VR(url)    elif mode==65:pornhd.SCRAPE_PORNHD_CATS()    elif mode==66:pornhd.SCRAPE_PORNHD_CONTENT(url)    elif mode==67:pornhd.SCRAPE_PORNHD_PLAY_CONTENT(name,url,iconimage,fanart)    elif mode==68:porncom.SCRAPE_PORNCOM_CATS()    elif mode==69:porncom.SCRAPE_PORNCOM_VIDS(url)    elif mode==70:porncom.SCRAPE_PORNCOM_LINKS(name,url,iconimage)    elif mode==71:youtube.YOUTUBE_CHANNEL(url)    elif mode==72:youtube.YOUTUBE_CHANNEL_PART2(url)    elif mode==73:musicvids.SCRAPE_MUSICVIDS_CATS(url)    elif mode==74:musicvids.SCRAPE_MUSICVIDS_LINKS(url)    elif mode==75:musicvids.SCRAPE_MUSICVIDS_PLAY(url)    elif mode==76:pawpatrol.SCRAPE_PAWPATROL()    elif mode==77:pawpatrol.SCRAPE_PAWPATROL_EPI(url,iconimage)    elif mode==78:pawpatrol.SCRAPE_PAWPATROL_PLAY(url)    elif mode==79:transfers.SCRAPE_TRANSFERS()    elif mode==80:transfers.TRANSFERS_POPUP(url)    elif mode==81:eporner.EPORNER_CATS()    elif mode==82:eporner.EPORNER_VIDS(url)    elif mode==83:eporner.EPORNER_LINKS(url,iconimage)    elif mode==84:tvbox.SCRAPE_TVBOX_CATS(url)    elif mode==85:tvbox.SCRAPE_TVBOX_LINKS(url,iconimage)    elif mode==86:tvbox.SCRAPE_TVBOX_PLAY(url,iconimage)