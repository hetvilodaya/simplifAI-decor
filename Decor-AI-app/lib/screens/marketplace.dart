import 'package:codeshastra/screens/item_ui_design_widget.dart';
import 'package:codeshastra/screens/items.dart';
import 'package:codeshastra/screens/items_upload_screen.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:codeshastra/utils/constants.dart';
import 'package:flutter/material.dart';

class MarketPlace extends StatefulWidget {
  const MarketPlace({Key? key}) : super(key: key);

  @override
  State<MarketPlace> createState() => _MarketPlaceState();
}

class _MarketPlaceState extends State<MarketPlace> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          automaticallyImplyLeading: false,
          backgroundColor: white,
          elevation: 0,
          centerTitle: true,
          toolbarHeight: 60,
          title: Padding(
            padding: const EdgeInsets.all(20),
            child: Text(
              "Marketplace",
              style: const TextStyle(
                color: darkblue,
                fontSize: 35.0,
                fontWeight: FontWeight.w700,
              ),
            ),
          ),
          actions: [
            IconButton(
              onPressed: () {
                Navigator.push(context,
                    MaterialPageRoute(builder: (c) => ItemsUploadScreen()));
              },
              icon: const Icon(
                Icons.add,
                color: darkblue,
              ),
            ),
          ],
        ),
        body: GridView.builder(
          physics: BouncingScrollPhysics(),
          gridDelegate:
              SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2),
          itemCount: 3,
          itemBuilder: (context, index) {
            Items eachItemInfo = products[index];

            return ItemUIDesignWidget(
              itemsInfo: eachItemInfo,
              context: context,
            );
          },
        ));
  }
  // else {
  //   return Column(
  //     crossAxisAlignment: CrossAxisAlignment.center,
  //     children: const [
  //       Center(
  //         child: Text(
  //           "Data is not available.",
  //           style: TextStyle(
  //             fontSize: 30,
  //             color: Colors.grey,
  //           ),
  //         ),
  //       ),
  //     ],
  //   );
  // }
}
