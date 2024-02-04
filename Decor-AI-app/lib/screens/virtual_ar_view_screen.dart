import 'package:augmented_reality_plugin/augmented_reality_plugin.dart';
import 'package:codeshastra/utils/constants.dart';
import 'package:flutter/material.dart';

class VirtualARViewScreen extends StatefulWidget {
  String? clickedItemImageLink;

  VirtualARViewScreen({
    this.clickedItemImageLink,
  });

  @override
  State<VirtualARViewScreen> createState() => _VirtualARViewScreenState();
}

class _VirtualARViewScreenState extends State<VirtualARViewScreen> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          centerTitle: true,
          title: const Text(
            "AR View",
            style: TextStyle(
              color: darkblue,
              fontWeight: FontWeight.w700,
              fontSize: 35,
            ),
          ),
          leading: IconButton(
            icon: const Icon(
              Icons.arrow_back_ios,
              color: darkblue,
            ),
            onPressed: () {
              Navigator.pop(context);
            },
          ),
        ),
        body: AugmentedRealityPlugin(
          'https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fsofa-removebg-preview.png?alt=media&token=347e8613-5204-4bda-9e92-4b6287bb8659',
        ));
  }
}
