# sharedapi-client
A high performance & centrally cached API service for premium bots. 

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version:  commit e9b768a rl @ Sep 3 3:07 pm
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/monty-dev/sharedapi_client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/monty-dev/sharedapi_client.git`)

Then import the package:
```python
import sharedapi_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import sharedapi_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import sharedapi_client
from sharedapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://dev.melaniebot.net
# See configuration.py for a list of all supported configuration parameters.
configuration = sharedapi_client.Configuration(
    host = "https://dev.melaniebot.net"
)



# Enter a context with an instance of the API client
async with sharedapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = sharedapi_client.AdminApi(api_client)
    target = None # object | 

    try:
        # Delete A Media Cache Object
        api_response = await api_instance.deleteamediacacheobject(target)
        print("The response of AdminApi->deleteamediacacheobject:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdminApi->deleteamediacacheobject: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://dev.melaniebot.net*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminApi* | [**deleteamediacacheobject**](docs/AdminApi.md#deleteamediacacheobject) | **DELETE** /api/admin/cache/{target} | Delete A Media Cache Object
*AdminApi* | [**get_rp_cendpoint**](docs/AdminApi.md#get_rp_cendpoint) | **GET** /api/admin/rpc | Get Rpc Endpoint
*AiApi* | [**createartwithdalle2**](docs/AiApi.md#createartwithdalle2) | **GET** /api/ai/dalle-2 | Create Art With Dalle-2
*AiApi* | [**createcyberpunkavatar**](docs/AiApi.md#createcyberpunkavatar) | **GET** /api/ai/cyberpunk | Create Cyberpunk Avatar
*AiApi* | [**createfantasyartavatar**](docs/AiApi.md#createfantasyartavatar) | **GET** /api/ai/creative | Create Fantasy Art Avatar
*AiApi* | [**createpixelavatar**](docs/AiApi.md#createpixelavatar) | **GET** /api/ai/avatar | Create Pixel Avatar
*AiApi* | [**evaluate_image_safety**](docs/AiApi.md#evaluate_image_safety) | **GET** /api/ai/nsfw_check | Evaluate Image Safety
*AiApi* | [**read_textfrom_image**](docs/AiApi.md#read_textfrom_image) | **POST** /api/ai/ocr | Read Text From Image
*AiApi* | [**removebackgroundsfromimage**](docs/AiApi.md#removebackgroundsfromimage) | **GET** /api/ai/segment_bg | Remove Backgrounds From Image
*DiscordApi* | [**fetch_discord_bio**](docs/DiscordApi.md#fetch_discord_bio) | **GET** /api/discord/bio | Fetch Discord Bio
*DiscordApi* | [**issue_clear_snipe**](docs/DiscordApi.md#issue_clear_snipe) | **DELETE** /api/discord/clearsnipe | Issue Clear Snipe
*InstagramApi* | [**download_instagram_post**](docs/InstagramApi.md#download_instagram_post) | **POST** /api/instagram/post | Download Instagram Post
*InstagramApi* | [**fetch_stories**](docs/InstagramApi.md#fetch_stories) | **GET** /api/instagram/story/{username} | Fetch Stories
*InstagramApi* | [**get_highlightby_id**](docs/InstagramApi.md#get_highlightby_id) | **GET** /api/instagram/highlight/{highlight_id} | Get Highlight By Id
*InstagramApi* | [**get_highlights**](docs/InstagramApi.md#get_highlights) | **GET** /api/instagram/highlights/{username} | Get Highlights
*InstagramApi* | [**get_instagram_user**](docs/InstagramApi.md#get_instagram_user) | **GET** /api/instagram/{username} | Get Instagram User
*PinterestApi* | [**get_pinterestuser**](docs/PinterestApi.md#get_pinterestuser) | **GET** /api/pinterest/{username} | Get Pinterest User
*PinterestApi* | [**reverse_imagesearch**](docs/PinterestApi.md#reverse_imagesearch) | **GET** /api/pinterest/reverse | Reverse Image Search
*RobloxApi* | [**get_robloxuser**](docs/RobloxApi.md#get_robloxuser) | **GET** /api/roblox/{username} | Get Roblox User
*SnapchatApi* | [**get_snapuser**](docs/SnapchatApi.md#get_snapuser) | **GET** /api/snap/{username} | Get Snapuser
*SpeechApi* | [**perform_speechto_text**](docs/SpeechApi.md#perform_speechto_text) | **GET** /api/speech/stt | Perform Speech To Text
*SpeechApi* | [**perform_textto_speech**](docs/SpeechApi.md#perform_textto_speech) | **POST** /api/speech/tts | Perform Text To Speech
*TiktokApi* | [**download_tik_tok_post**](docs/TiktokApi.md#download_tik_tok_post) | **POST** /api/tiktok/post | Download Tiktok Post
*TiktokApi* | [**fetch_user_top_tik_toks**](docs/TiktokApi.md#fetch_user_top_tik_toks) | **GET** /api/tiktok/{username}/top | Fetch User Top Tiktoks
*TiktokApi* | [**get_tik_tok_user**](docs/TiktokApi.md#get_tik_tok_user) | **GET** /api/tiktok/{username} | Get Tiktok User
*TiktokApi* | [**getrecentuser_tik_toks**](docs/TiktokApi.md#getrecentuser_tik_toks) | **GET** /api/tiktok/{username}/recent | Get Recent User Tiktoks
*TwitterApi* | [**fetch_twitteruser**](docs/TwitterApi.md#fetch_twitteruser) | **GET** /api/twitter/{username} | Fetch Twitter User
*ValorantApi* | [**get_valorantuser**](docs/ValorantApi.md#get_valorantuser) | **GET** /api/valorant/{agent}/{tag} | Get Valorant User
*WebApi* | [**get_cashappprofile**](docs/WebApi.md#get_cashappprofile) | **GET** /api/cashapp/{username} | Get Cashapp Profile
*WebApi* | [**get_telegram_u_ser**](docs/WebApi.md#get_telegram_u_ser) | **GET** /api/web/telegram/{username} | Get Telegram User
*WebApi* | [**i_plookup**](docs/WebApi.md#i_plookup) | **GET** /api/web/ip/{address} | Ip Lookup
*WebApi* | [**loada_spotifyplaylist**](docs/WebApi.md#loada_spotifyplaylist) | **GET** /api/spotify/playlist/{playlist_id} | Load A Spotify Playlist
*WebApi* | [**screenshotweb**](docs/WebApi.md#screenshotweb) | **GET** /api/web/screenshot | Screenshot Web
*WebApi* | [**streamaudio**](docs/WebApi.md#streamaudio) | **GET** /fragementStream | Stream Audio
*YoutubeApi* | [**search_you_tube**](docs/YoutubeApi.md#search_you_tube) | **POST** /api/youtube/search | Search Youtube


## Documentation For Models

 - [AIImageGenerationResponse](docs/AIImageGenerationResponse.md)
 - [ActRankWin](docs/ActRankWin.md)
 - [ActivityAsset](docs/ActivityAsset.md)
 - [AdvancedInfo](docs/AdvancedInfo.md)
 - [Author](docs/Author.md)
 - [Avatar](docs/Avatar.md)
 - [BadgeItem](docs/BadgeItem.md)
 - [BannerType](docs/BannerType.md)
 - [BioMember](docs/BioMember.md)
 - [BioRequest](docs/BioRequest.md)
 - [BioResponse](docs/BioResponse.md)
 - [BioUser](docs/BioUser.md)
 - [CacheDelete](docs/CacheDelete.md)
 - [Caption](docs/Caption.md)
 - [CashAppProfile](docs/CashAppProfile.md)
 - [CashappProfileResponse](docs/CashappProfileResponse.md)
 - [ColorPalette](docs/ColorPalette.md)
 - [ConnectedAccount](docs/ConnectedAccount.md)
 - [CountryCurrency](docs/CountryCurrency.md)
 - [CountryFlag](docs/CountryFlag.md)
 - [CurrentData](docs/CurrentData.md)
 - [DatumImages](docs/DatumImages.md)
 - [DeletionConfirmation](docs/DeletionConfirmation.md)
 - [DiscordUser](docs/DiscordUser.md)
 - [DownloaderOptions](docs/DownloaderOptions.md)
 - [DownloaderOptions1](docs/DownloaderOptions1.md)
 - [E1A1](docs/E1A1.md)
 - [Format](docs/Format.md)
 - [Fragment](docs/Fragment.md)
 - [GatewayUserStatus](docs/GatewayUserStatus.md)
 - [GuildMember](docs/GuildMember.md)
 - [GuildMemberProfile](docs/GuildMemberProfile.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [HighestRank](docs/HighestRank.md)
 - [HighlightItem](docs/HighlightItem.md)
 - [HttpHeaders](docs/HttpHeaders.md)
 - [HttpHeaders1](docs/HttpHeaders1.md)
 - [IPLookupResultResponse](docs/IPLookupResultResponse.md)
 - [Image](docs/Image.md)
 - [ImageEvaluationResult](docs/ImageEvaluationResult.md)
 - [ImagePostInfo](docs/ImagePostInfo.md)
 - [InstagramCarouselMediaResponse](docs/InstagramCarouselMediaResponse.md)
 - [InstagramHighlightIndexResponse](docs/InstagramHighlightIndexResponse.md)
 - [InstagramHighlightMediaItem](docs/InstagramHighlightMediaItem.md)
 - [InstagramHighlightResponse](docs/InstagramHighlightResponse.md)
 - [InstagramPostItem](docs/InstagramPostItem.md)
 - [InstagramPostRequest](docs/InstagramPostRequest.md)
 - [InstagramPostResponse](docs/InstagramPostResponse.md)
 - [InstagramProfileModelResponse](docs/InstagramProfileModelResponse.md)
 - [InstagramStoryResponse](docs/InstagramStoryResponse.md)
 - [InstagramUserResponse](docs/InstagramUserResponse.md)
 - [IpScamScore](docs/IpScamScore.md)
 - [LiveChat](docs/LiveChat.md)
 - [MMRData](docs/MMRData.md)
 - [MelanieActivity](docs/MelanieActivity.md)
 - [MelanieEmoji](docs/MelanieEmoji.md)
 - [MelanieModelsSharedapiTwitterScreenNameBirthdate](docs/MelanieModelsSharedapiTwitterScreenNameBirthdate.md)
 - [MelanieModelsSharedapiTwitterScreenNameDescriptionEntity](docs/MelanieModelsSharedapiTwitterScreenNameDescriptionEntity.md)
 - [MelanieModelsSharedapiTwitterScreenNameEntities](docs/MelanieModelsSharedapiTwitterScreenNameEntities.md)
 - [MelanieModelsSharedapiTwitterScreenNameFluffyRef](docs/MelanieModelsSharedapiTwitterScreenNameFluffyRef.md)
 - [MelanieModelsSharedapiTwitterScreenNameHighlightsInfo](docs/MelanieModelsSharedapiTwitterScreenNameHighlightsInfo.md)
 - [MelanieModelsSharedapiTwitterScreenNameLegacy](docs/MelanieModelsSharedapiTwitterScreenNameLegacy.md)
 - [MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile](docs/MelanieModelsSharedapiTwitterScreenNameLegacyExtendedProfile.md)
 - [MelanieModelsSharedapiTwitterScreenNamePurpleRef](docs/MelanieModelsSharedapiTwitterScreenNamePurpleRef.md)
 - [MelanieModelsSharedapiTwitterScreenNameReason](docs/MelanieModelsSharedapiTwitterScreenNameReason.md)
 - [MelanieModelsSharedapiTwitterScreenNameReasonDescription](docs/MelanieModelsSharedapiTwitterScreenNameReasonDescription.md)
 - [MelanieModelsSharedapiTwitterScreenNameURL](docs/MelanieModelsSharedapiTwitterScreenNameURL.md)
 - [MelanieModelsSharedapiTwitterScreenNameURLClass](docs/MelanieModelsSharedapiTwitterScreenNameURLClass.md)
 - [MelanieModelsSharedapiTwitterScreenNameUnavailableMessage](docs/MelanieModelsSharedapiTwitterScreenNameUnavailableMessage.md)
 - [MelanieModelsSharedapiTwitterScreenNameUnavailableMessageEntity](docs/MelanieModelsSharedapiTwitterScreenNameUnavailableMessageEntity.md)
 - [MelanieModelsSharedapiTwitterScreenNameVerificationInfo](docs/MelanieModelsSharedapiTwitterScreenNameVerificationInfo.md)
 - [MelanieModelsSharedapiTwitterUserTweetsBirthdate](docs/MelanieModelsSharedapiTwitterUserTweetsBirthdate.md)
 - [MelanieModelsSharedapiTwitterUserTweetsDescriptionEntity](docs/MelanieModelsSharedapiTwitterUserTweetsDescriptionEntity.md)
 - [MelanieModelsSharedapiTwitterUserTweetsEntities](docs/MelanieModelsSharedapiTwitterUserTweetsEntities.md)
 - [MelanieModelsSharedapiTwitterUserTweetsFluffyRef](docs/MelanieModelsSharedapiTwitterUserTweetsFluffyRef.md)
 - [MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo](docs/MelanieModelsSharedapiTwitterUserTweetsHighlightsInfo.md)
 - [MelanieModelsSharedapiTwitterUserTweetsLegacy](docs/MelanieModelsSharedapiTwitterUserTweetsLegacy.md)
 - [MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile](docs/MelanieModelsSharedapiTwitterUserTweetsLegacyExtendedProfile.md)
 - [MelanieModelsSharedapiTwitterUserTweetsPurpleRef](docs/MelanieModelsSharedapiTwitterUserTweetsPurpleRef.md)
 - [MelanieModelsSharedapiTwitterUserTweetsReason](docs/MelanieModelsSharedapiTwitterUserTweetsReason.md)
 - [MelanieModelsSharedapiTwitterUserTweetsReasonDescription](docs/MelanieModelsSharedapiTwitterUserTweetsReasonDescription.md)
 - [MelanieModelsSharedapiTwitterUserTweetsURL](docs/MelanieModelsSharedapiTwitterUserTweetsURL.md)
 - [MelanieModelsSharedapiTwitterUserTweetsURLClass](docs/MelanieModelsSharedapiTwitterUserTweetsURLClass.md)
 - [MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage](docs/MelanieModelsSharedapiTwitterUserTweetsUnavailableMessage.md)
 - [MelanieModelsSharedapiTwitterUserTweetsUnavailableMessageEntity](docs/MelanieModelsSharedapiTwitterUserTweetsUnavailableMessageEntity.md)
 - [MelanieModelsSharedapiTwitterUserTweetsVerificationInfo](docs/MelanieModelsSharedapiTwitterUserTweetsVerificationInfo.md)
 - [MelanieModelsSharedapiValorant2Card](docs/MelanieModelsSharedapiValorant2Card.md)
 - [MelanieModelsSharedapiValorantCard](docs/MelanieModelsSharedapiValorantCard.md)
 - [Music](docs/Music.md)
 - [OCRReadResponse](docs/OCRReadResponse.md)
 - [OCRRquest](docs/OCRRquest.md)
 - [PinterestProfileResponse](docs/PinterestProfileResponse.md)
 - [PinterestReverseItem](docs/PinterestReverseItem.md)
 - [PinterestReverseResponse](docs/PinterestReverseResponse.md)
 - [ProfileModel](docs/ProfileModel.md)
 - [PuppeteerLoadMethod](docs/PuppeteerLoadMethod.md)
 - [RobloxUserProfileResponse](docs/RobloxUserProfileResponse.md)
 - [STTResult](docs/STTResult.md)
 - [SearchResult](docs/SearchResult.md)
 - [SnapProfileResponse](docs/SnapProfileResponse.md)
 - [Speakers](docs/Speakers.md)
 - [SpotifyData](docs/SpotifyData.md)
 - [Statistics](docs/Statistics.md)
 - [StoryItem](docs/StoryItem.md)
 - [Subtitles](docs/Subtitles.md)
 - [TTSResult](docs/TTSResult.md)
 - [TTSTranslationRequest](docs/TTSTranslationRequest.md)
 - [TelegramProfileResponse](docs/TelegramProfileResponse.md)
 - [Thumbnail](docs/Thumbnail.md)
 - [TikTokTopVideoItem](docs/TikTokTopVideoItem.md)
 - [TikTokUserProfileResponse](docs/TikTokUserProfileResponse.md)
 - [TikTokVideoResponse](docs/TikTokVideoResponse.md)
 - [TiktokPostRequest](docs/TiktokPostRequest.md)
 - [TiktokTopUserVideoResults](docs/TiktokTopUserVideoResults.md)
 - [TweetDataResult](docs/TweetDataResult.md)
 - [TwitterUserDataRaw](docs/TwitterUserDataRaw.md)
 - [TwitterUserinfoResult](docs/TwitterUserinfoResult.md)
 - [User1](docs/User1.md)
 - [UserPostItem](docs/UserPostItem.md)
 - [UserProfile](docs/UserProfile.md)
 - [UserinfoData](docs/UserinfoData.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValorantProfileResponse](docs/ValorantProfileResponse.md)
 - [Video](docs/Video.md)
 - [VideoIcon](docs/VideoIcon.md)
 - [YTSearchRequest](docs/YTSearchRequest.md)
 - [YoutubeSearchResults](docs/YoutubeSearchResults.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




