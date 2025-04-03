using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Projekt
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
            comboBox1.Items.Add("Jinx");
            comboBox1.Items.Add("Aatrox");
            comboBox1.Items.Add("Aphelios");

            comboBox1.SelectedIndexChanged+=comboBox1_SelectedIndexChanged;

        }

        private void comboBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
           string selectedForm=  comboBox1.SelectedItem.ToString();
            Form newForm = null;

            foreach (Form openForm in Application.OpenForms)
            {
                if (openForm.Text == selectedForm)
                {
                    openForm.Focus();
                    return;

                }
            }
            switch(selectedForm) 
            {
                case "Jinx":
                    newForm = new Jinx();
                    break;

                case "Aatrox":
                    newForm=new Aatrox();
                    break;

                case "Aphelios":
                    newForm = new Form1();
                    break;
            }
            if (newForm!=null)
            {
                newForm.Show();
                this.Hide();

            }
        }

        private void button1_Click(object sender, EventArgs e)
        {

        }

        private void pictureBox3_Click(object sender, EventArgs e)
        {

        }

        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label2_Click(object sender, EventArgs e)
        {

        }

        private void textBox1_TextChanged(object sender, EventArgs e)
        {

        }
    }
}
