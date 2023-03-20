package pl.meblowy;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.io.IOException;

public class FurnitureStorePage extends JFrame {
    private JPanel MainWindow;
    private JButton addButton;
    private JTable contentsTable;
    private JTextField nameTextField;
    private JTextField materialTextField;
    private JTextField weightTextField;
    private JTextField priceTextField;
    private JComboBox furnitureComboBox;
    private JButton readButton;
    private JButton saveButton;
    private JLabel ErrorLabel;
    private JButton deleteButton;
    private pl.meblowy.FurnitureStore FStore;
    private FStoreFileManager FFSManager;
    private final DefaultTableModel model = new DefaultTableModel();

    public FurnitureStorePage() {
        setupFrame();
        addButton.addActionListener(e -> addToTable());
        deleteButton.addActionListener(e -> deleteRowFromTable());
        nameTextField.addActionListener(e -> materialTextField.grabFocus());
        materialTextField.addActionListener(e -> weightTextField.grabFocus());
        weightTextField.addActionListener(e -> priceTextField.grabFocus());
        priceTextField.addActionListener(e -> furnitureComboBox.grabFocus());
        priceTextField.addActionListener(e -> addToTable());
        readButton.addActionListener(e -> read());
        saveButton.addActionListener(e -> save());
    }


    private void setupFrame() {
        //setup
        setContentPane(MainWindow);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setMinimumSize(new Dimension(600, 400));
        setVisible(true);
        contentsTable.setModel(model);
        model.setColumnCount(5);
        FStore = new FurnitureStore();
        FFSManager = new FStoreFileManager(".//chairs", ".//tables");
    }

    private void addToTable() {
        try {
            Object furniture = furnitureComboBox.getSelectedItem();
            String name = Checker.returnBoxText(nameTextField.getText());
            String material = Checker.returnBoxText(materialTextField.getText());
            String weight = weightTextField.getText();
            String price = priceTextField.getText();


            Integer weightInt = Integer.parseInt(weight);
            Integer priceInt = Integer.parseInt(price);

            assert furniture != null;
            String strFurniture = furniture.toString();
            if (strFurniture.equals("-----")) {
                throw new IllegalArgumentException() {
                };
            }
            FStore.createFurniture(furniture, name, material, weightInt, priceInt);
            addRowToTable(furniture, name, material, weightInt, priceInt);
            ErrorLabel.setText("");
        } catch (NumberFormatException e) {
            ErrorLabel.setText("Expected integer, got something else.");
        } catch (IllegalArgumentException e) {
            ErrorLabel.setText("You cannot choose ----- option.");
        } catch (EmptyBoxException e) {
            ErrorLabel.setText(e.toString());
        }


        nameTextField.setText("");
        materialTextField.setText("");
        weightTextField.setText("");
        priceTextField.setText("");
        furnitureComboBox.setSelectedIndex(0);
        nameTextField.grabFocus();

    }

    private void addRowToTable(Object furniture, String name, String material, Integer weight, Integer price) {
        Object[] row = new Object[]{furniture, name, material, weight, price};
        model.addRow(row);
    }

    private void deleteRowFromTable() {
        DefaultTableModel localModel = (DefaultTableModel) contentsTable.getModel();
        if (contentsTable.getSelectedRowCount() == 1) {
            localModel.removeRow(contentsTable.getSelectedRow());
        } else if (contentsTable.getRowCount() == 0) {
            ErrorLabel.setText("There is no data in the table to erase");
        } else if (contentsTable.getSelectedRowCount() > 1) {
            ErrorLabel.setText("You can only pick one row to delete.");
        } else if (contentsTable.getSelectedRowCount() == 0) {
            ErrorLabel.setText("You did not pick a row");
        }


    }

    private void read() {
        try {
            this.FStore = FFSManager.readFromFile();
        } catch (IOException | ClassNotFoundException exc) {
            ErrorLabel.setText("Couldn't read a file");
        }
        restoreTable();
    }

    private void save() {
        try {
            FFSManager.saveToFile(this.FStore);
        } catch (IOException exc) {
            ErrorLabel.setText("Couldn't save a file");
        }
    }

    private void restoreTable() {
        for (int i = 0; i < FStore.chairs.size(); i++) {
            Object[] row = {
                    "Chair",
                    FStore.chairs.get(i).returnName(),
                    FStore.chairs.get(i).returnMaterial(),
                    FStore.chairs.get(i).returnChairWeight(),
                    FStore.chairs.get(i).returnChairPrice()
            };
            model.addRow(row);
        }
        for (int i = 0; i < FStore.tables.size(); i++) {
            Object[] row = {
                    "Table",
                    FStore.tables.get(i).returnName(),
                    FStore.tables.get(i).returnMaterial(),
                    FStore.tables.get(i).returnTableWeight(),
                    FStore.tables.get(i).returnTablePrice()
            };
            model.addRow(row);
        }
    }
}

