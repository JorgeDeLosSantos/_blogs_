function java_ex
init()

    function init()
        import java.awt.*
        import javax.swing.*
        
        frame = JFrame('Java Example');
        
        p1 = JPanel();
        p2 = JPanel();
        p1.setLayout(BoxLayout(p1, BoxLayout.Y_AXIS));
        p2.setLayout(BoxLayout(p2, BoxLayout.X_AXIS));
        
        labels = {'a','b','c','d','e'};
        
        buttons = cell(size(labels));
        for k=1:length(labels)
            buttons{k} = JButton(labels{k});
            p1.add(buttons{k});
        end
        
        buttons2 = cell(size(labels));
        for k=1:length(labels)
            buttons2{k} = JButton(labels{k});
            p2.add(buttons2{k});
        end
        %         hb1 = handle(b1,'CallbackProperties');
        %         hb2 = handle(b2,'CallbackProperties');
        %         set(hb1, 'ActionPerformedCallback',@);
        %         set(hb2, 'ActionPerformedCallback','disp(345)');
        p1.setBackground(Color.RED);
        frame.setLayout(FlowLayout());
        frame.add(p1);
        frame.add(p2);
        frame.setVisible(true);
        frame.setSize(300,200);
        frame.setLocationRelativeTo([]);
    end

end