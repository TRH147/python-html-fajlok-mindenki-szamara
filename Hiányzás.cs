using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace Gyakorlás3
{
    public partial class Hiányzás : Form
    {
        public Hiányzás()
        {
            InitializeComponent();
        }
        List<Hianyzasok> hianyzasok = new List<Hianyzasok>();
        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void Hiányzás_Load(object sender, EventArgs e)
        {
            string[] sorok = File.ReadAllLines("hianyzasok.txt");
            foreach (string s in sorok)
            {
                string[] adatok = s.Split(',');
                Hianyzasok hianyzas = new Hianyzasok(adatok[0], adatok[1], adatok[2], adatok[3], adatok[4]);
                hianyzasok.Add(hianyzas);
            }

            foreach (var h in hianyzasok)
            {
                dataGridView1.Rows.Add(h.sorszam, h.nev, h.igazolatlanh, h.igazolth, h.szuldatum);
            }

        }

        private void button1_Click(object sender, EventArgs e)
        {
            DateTime bekertszuldate = Convert.ToDateTime(textBox2.Text);

            foreach (var item in hianyzasok)
            {
                if (bekertszuldate == item.szuldatum)
                {
                    if (item.igazolatlanh < 10)
                    {
                        label1.Text = ("5-ös magatartás");
                    }
                    else if (item.igazolatlanh >= 10 && item.igazolatlanh <= 14)
                    {
                        label1.Text = ("4-es magatartás, figyelmeztetésben részesítem");
                    }
                    else if (item.igazolatlanh >= 15 && item.igazolatlanh <= 18)
                    {
                        label1.Text = ("3-as magatartás, osztályfőnökiben részesül");
                    }
                    else if (item.igazolatlanh >= 19 && item.igazolatlanh <= 25)
                    {
                        label1.Text = ("2-es magatartás, igazgatói megrovás");
                    }
                    else 
                    {
                        label1.Text = ("Felfüggesztés");
                    }
                }
            }
        }
    }
}
