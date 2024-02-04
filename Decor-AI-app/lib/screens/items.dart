import 'package:cloud_firestore/cloud_firestore.dart';

class Items {
  String? itemID;
  String? itemName;
  String? itemDescription;
  String? itemImage;
  String? sellerName;
  String? sellerPhone;
  String? itemPrice;
  Timestamp? publishedDate;
  String? status;

  Items({
    this.itemID,
    this.itemName,
    this.itemDescription,
    this.itemImage,
    this.sellerName,
    this.sellerPhone,
    this.itemPrice,
  });

  Items.fromJson(Map<String, dynamic> json) {
    itemID = json["itemID"];
    itemName = json["itemName"];
    itemDescription = json["itemDescription"];
    itemImage = json["itemImage"];
    sellerName = json["sellerName"];
    sellerPhone = json["sellerPhone"];
    itemPrice = json["itemPrice"];
  }
}

List<Items> products = [
  Items(
    itemID: "1",
    itemName: "Sofa",
    itemDescription: "Wonderful",
    itemImage:
        "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fsofa-removebg-preview.png?alt=media&token=347e8613-5204-4bda-9e92-4b6287bb8659",
    sellerName: "Nishtha",
    sellerPhone: "9876543210",
    itemPrice: "5000",
  ),
  Items(
    itemID: "2",
    itemName: "Dining table",
    itemDescription: "Wonderful",
    itemImage:
        "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fdining-removebg-preview.png?alt=media&token=dd432452-bcbd-4af9-b8fb-aa453db71341",
    sellerName: "Nishtha",
    sellerPhone: "9876543210",
    itemPrice: "4000",
  ),
  Items(
    itemID: "1",
    itemName: "Drawer",
    itemDescription: "Wonderful",
    itemImage:
        "https://firebasestorage.googleapis.com/v0/b/coffeeft-31b1e.appspot.com/o/videos%2Fdrawer-removebg-preview.png?alt=media&token=797026c7-0ad3-4931-8813-a5df1bdba09b",
    sellerName: "Nishtha",
    sellerPhone: "9876543210",
    itemPrice: "7000",
  ),
];
