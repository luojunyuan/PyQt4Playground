/** omajinai.qml
 *  9/29/2012 jichi
 *  A hello world example to demonstrate how to render animated subtitles
 */
import QtQuick 1.1
// import '../imports/qmleffects' as Effects

Rectangle { id: root_
  color: 'transparent'
  width: 500; height: 400

  // Window properties
  // this is for python file
  property string windowTitle: qsTr("Magic Text")
  property bool translucent: true
  property bool fullScreen: true
  property bool ignoresFocus: true
  property int windowFlags:
    Qt.SplashScreen | // no focus; alternatlvely, use Qt.Popup for autohide
    Qt.FramelessWindowHint |
    Qt.WindowStaysOnTop

  property color pressColor: '#2d5f5f'
  property color releaseColor: 'orange'

  // Automatically hide after 15 seconds
  // Timer { id: timer_
  //   running: true; repeat: false
  //   interval: 15000
  //   onTriggered: Qt.quit()
  // }

  Component.onCompleted: console.log("applet:magictext.qml: pass")

  Keys.onPressed: {
    if (event.key === Qt.Key_Delete || event.key === Qt.Key_Backspace)
      text_.remove()
    else if (event.text !== "") {
      text_.append(event.text)
    }
  }

  // - Animated Text -
  Item { id: text_
    anchors.margins: 15
    anchors.top: parent.top
    property string text:
        "*(。ﾟωﾟ) ｡ Nomobuyo, woshi, hashitawa, dogeda, gunmicha, de, ribura!!"

    property bool animated: true

    function append(text) {
      text_.animated = false
      var lastLetter = text_.children[text_.children.length - 1]
      var newLetter = letterComponent_.createObject(text_)
      newLetter.text = text
      newLetter.follow = lastLetter
      text_.animated = true
    }

    function remove() {
      if (text_.children.length)
        text_.children[text_.children.length - 1].destroy()
    }

    function doLayout() {
      var follow = null
      for (var i = 0; i < text_.text.length; ++i) {
        var newLetter = letterComponent_.createObject(text_)
        newLetter.text = text_.text[i]
        newLetter.follow = follow
        follow = newLetter
      }
    }

    Component { id: letterComponent_
      Text { id: letter_
        property variant follow

        x: follow ? follow.x + follow.width : text_.width / 3
        y: follow ? follow.y : text_.height / 2

        font.pixelSize: 40; font.bold: true; //font.italic: true
        style: Text.Raised

        color: 'black'
        styleColor: root_.releaseColor

        // effect: Effects.TextShadow {
        //   blurRadius: 8
        //   offset: '1,1'
        //   color: 'red'
        // }

        MouseArea {
          anchors.fill: parent
          drag.target: letter_; drag.axis: Drag.XandYAxis
          onPressed: { letter_.styleColor = root_.pressColor }
          onReleased: { letter_.styleColor = root_.releaseColor }
        }

        Behavior on x { enabled: text_.animated; SpringAnimation { spring: 3; damping: 0.3; mass: 1.0 } }
        Behavior on y { enabled: text_.animated; SpringAnimation { spring: 3; damping: 0.3; mass: 1.0 } }
      }
    }

    Component.onCompleted: doLayout()
  }
}

