package javafx_applications.HelloWorld;

import java.applet.*;
import java.awt.*;
import java.util.Date;

/*
<applet code="HelloWorld" width=200 height=60>
</applet>
*/

// HelloWorld class extends Applet
public class HelloWorld extends Applet {
    // Overriding paint() method
    @Override
    public void paint(Graphics g) {
        g.drawString("Hello World", 20, 20);
        Date dt = new Date();
        super.showStatus("Today is" + dt);
    }

}
