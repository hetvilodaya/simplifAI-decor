import 'package:flutter/material.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:flutter/src/widgets/placeholder.dart';
import 'package:codeshastra/screens/video_player.dart';

import '../utils/constants.dart';
// import 'package:trinity/screens/video_player.dart';
// import 'package:video_player/video_player.dart';

class Videos extends StatefulWidget {
  const Videos({super.key});

  @override
  State<Videos> createState() => _VideosState();
}

class _VideosState extends State<Videos> {
  // var _razorpay = Razorpay();
  @override
  Widget build(BuildContext context) {
    PageController _pageController = PageController(initialPage: 0);
    List<Widget> reel = [
      VideoScreen(
          url:
              "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fvideo1.mp4?alt=media&token=bfc011ac-7b15-42a1-8426-2e2d138ee629"),
      VideoScreen(
          url:
              "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fvideo2.mp4?alt=media&token=b62c3ff0-97f7-4228-9753-b44d79d0f568"),
      VideoScreen(
          url:
              "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fvideo3.mp4?alt=media&token=1bb1e05b-6e3c-4563-bca9-4674bec4a171"),
      VideoScreen(
          url:
              "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fvideo4.mp4?alt=media&token=6e88fd00-835f-4510-994d-655e3f597a4e"),
      // VideoScreen(
      //     url:
      //         "https://firebasestorage.googleapis.com/v0/b/codeshastra-383011.appspot.com/o/Reels%2FWhatsApp%20Video%202023-04-08%20at%2023.25.54.mp4?alt=media&token=e2f91e60-aa6d-4fbb-a45e-75aecd72fc3e"),
    ];
    return Scaffold(
        backgroundColor: white,
        extendBodyBehindAppBar: true,
        appBar: AppBar(
          automaticallyImplyLeading: false,
          backgroundColor: Colors.transparent,
          elevation: 0,
          centerTitle: true,
          toolbarHeight: 60,
          title: Padding(
            padding: const EdgeInsets.symmetric(vertical: 20),
            child: Text(
              'Trending Decor',
              style: TextStyle(
                  fontWeight: FontWeight.bold,
                  color: darkblue,
                  fontSize: 35,
                  shadows: [
                    Shadow(
                        // bottomLeft
                        offset: Offset(-1.5, -1.5),
                        color: Colors.white),
                    Shadow(
                        // bottomRight
                        offset: Offset(1.5, -1.5),
                        color: Colors.white),
                    Shadow(
                        // topRight
                        offset: Offset(1.5, 1.5),
                        color: Colors.white),
                    Shadow(
                        // topLeft
                        offset: Offset(-1.5, 1.5),
                        color: Colors.white),
                  ]),
            ),
          ),
        ),
        body: PageView(
          controller: _pageController,
          scrollDirection: Axis.vertical,
          children: reel,
        ));
  }
}
