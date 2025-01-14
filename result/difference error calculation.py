import os
import pandas as pd
import csv
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using non-interactive Agg backend')
    mpl.use('Agg')
import matplotlib.pyplot as plt

font1 = {'weight' : 'normal',
'fontname' : 'Times New Roman',
'size' : 24,}

pig_ = 396669   # case number/name
case = [396669,396670,399018,399019,407034,407036,407037]
#path = input('Solve for ECHO or MRI: ')
for pig_ in case:
    if pig_ == 396669:
            total_t = 0.66925           
    elif pig_ == 396670:
            total_t = 0.4845
    elif pig_ == 399018:
            total_t = 0.5383
    elif pig_ == 399019:
            total_t = 0.5383
    elif pig_ == 407034:
            total_t = 0.5383
    elif pig_ == 407036:
            total_t = 0.48445
    elif pig_ == 407037:
            total_t = 0.5921
    kind=['echo','mri']
    for na in kind:
        if na.lower().strip() == 'echo':
            path = str(pig_)+'echo/'
        if na.lower().strip() == 'mri':
            path = str(pig_)+'mri/'
    
        STn='Ell'
        exdata = pd.read_csv(str(pig_)+'echo/'+'Strain_'+str(STn)+'.csv')
        hpdata = pd.read_csv(path+'HPCC_'+str(STn)+'.csv')
        
        n=0;aa=[];ab=[];lst=[];lst1=[]
        cc=0;t= total_t*1000/29
        while cc != len(exdata):
            ab.append(cc*t)
            cc+=1
        aa.append(ab)
        while n!=16:
            ex = np.array(exdata.values[:,n][1:])
            hp = np.array(hpdata.values[:,n][:29])
            aa.append(ex.tolist())
            aa.append(hp.tolist())
            n+=1
            
        STT = 'Ecc'           
        exdata = pd.read_csv(str(pig_)+'echo/'+'Strain_'+str(STT)+'.csv')
        hpdata = pd.read_csv(path+'HPCC_'+str(STT)+'.csv')
        n=0
        
        while n!=16:
            ex = np.array(exdata.values[:,n][1:])
            hp = np.array(hpdata.values[:,n][:29])
            aa.append(ex.tolist())
            aa.append(hp.tolist())
            n+=1
        
        fieldnames = []
        cnt =15
        m=0
        with open(path+'total_Strain.csv','w',newline='') as f:  
            for p in range(0, (len(aa))):
                
                fieldnames.append('Sector'+str(cnt))
                cnt += 1
            thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        
            while m!=(len(aa[0])-1):                 
                    thewriter.writerow({fieldnames[0]:aa[0][m],fieldnames[1]:aa[1][m],fieldnames[2]:aa[2][m],fieldnames[3]:aa[3][m],
                                        fieldnames[4]:aa[4][m],fieldnames[5]:aa[5][m],fieldnames[6]:aa[6][m],fieldnames[7]:aa[7][m],
                                        fieldnames[8]:aa[8][m],fieldnames[9]:aa[9][m],fieldnames[10]:aa[10][m],fieldnames[11]:aa[11][m],
                                        fieldnames[12]:aa[12][m],fieldnames[13]:aa[13][m],fieldnames[14]:aa[14][m],fieldnames[15]:aa[15][m],
                                        fieldnames[16]:aa[16][m],fieldnames[17]:aa[17][m],fieldnames[18]:aa[18][m],fieldnames[19]:aa[19][m],
                                        fieldnames[20]:aa[20][m],fieldnames[21]:aa[21][m],fieldnames[22]:aa[22][m],fieldnames[23]:aa[23][m],
                                        fieldnames[24]:aa[24][m],fieldnames[25]:aa[25][m],fieldnames[26]:aa[26][m],fieldnames[27]:aa[27][m],
                                        fieldnames[28]:aa[28][m],fieldnames[29]:aa[29][m],fieldnames[30]:aa[30][m],fieldnames[31]:aa[31][m],
                                        fieldnames[32]:aa[32][m],fieldnames[33]:aa[33][m],fieldnames[34]:aa[34][m],fieldnames[35]:aa[35][m],
                                        fieldnames[36]:aa[36][m],fieldnames[37]:aa[37][m],fieldnames[38]:aa[38][m],fieldnames[39]:aa[39][m],
                                        fieldnames[40]:aa[40][m],fieldnames[41]:aa[41][m],fieldnames[42]:aa[42][m],fieldnames[43]:aa[43][m],
                                        fieldnames[12+32]:aa[12+32][m],fieldnames[13+32]:aa[13+32][m],fieldnames[14+32]:aa[14+32][m],fieldnames[15+32]:aa[15+32][m],
                                        fieldnames[16+32]:aa[16+32][m],fieldnames[17+32]:aa[17+32][m],fieldnames[18+32]:aa[18+32][m],fieldnames[19+32]:aa[19+32][m],
                                        fieldnames[20+32]:aa[20+32][m],fieldnames[21+32]:aa[21+32][m],fieldnames[22+32]:aa[22+32][m],fieldnames[23+32]:aa[23+32][m],
                                        fieldnames[24+32]:aa[24+32][m],fieldnames[25+32]:aa[25+32][m],fieldnames[26+32]:aa[26+32][m],fieldnames[27+32]:aa[27+32][m],
                                        fieldnames[28+32]:aa[28+32][m],fieldnames[29+32]:aa[29+32][m],fieldnames[30+32]:aa[30+32][m],fieldnames[31+32]:aa[31+32][m],
                                        fieldnames[64]:aa[64][m]})
                    m+=1
        
        
        a=[];b=[];clst=[]
        ms=3;m=1
        PVdata = pd.read_csv(path+'PVLoop.csv')         # PV data for both simulation
        PVbdata = pd.read_csv(path+str(pig_)+'.csv')    # PV data for both measurment
        sdata = pd.read_csv(path+'total_Strain.csv')    # strain data for both simulation and measurment
        V = np.array(PVbdata.values[:,2][:30])
        P = np.array(PVbdata.values[:,1][:30])                   
        LVP = np.array(PVdata.values[:,1][18:])           
        LVV = np.array(PVdata.values[:,0][18:])               
        dcp=P-LVP; dcv= V-LVV
        a.append(dcp)
        a.append(P)
        b.append(dcv)
        b.append(V)
        ###############relative error between mearument and simulation
        x1=np.linalg.norm(x=a[0],ord=2,keepdims=False)
        x2=np.linalg.norm(x=a[1],ord=2,keepdims=False)
        x3=np.linalg.norm(x=b[0],ord=2,keepdims=False)
        x4=np.linalg.norm(x=b[1],ord=2,keepdims=False)
        Perror=x1/x2*100
        Verror=x3/x4 *100
        while m!= 65:
            S = np.array(sdata.values[:,m])
            num=m-1
            if (m%2)==0:
                S1=  np.array(sdata.values[:,num])
                SS=S-S1
                f =np.linalg.norm(x=SS,ord=2,keepdims=False)
                d =np.linalg.norm(x=S1,ord=2,keepdims=False)
                g=f/d*100
                clst.append(g)
            m+=1
        clst.append(Perror)
        clst.append(Verror)
        fieldnames = ['e']
        t=0
        
        with open(path+'Error.csv','w',newline='') as f:  
            thewriter = csv.DictWriter(f, fieldnames=fieldnames)
            while t!=(len(clst)):   
                
                thewriter.writerow({fieldnames[0]:clst[t]})
                t+=1
        
        ############################################### Strain Graphing
        sdata = pd.read_csv(path+'total_Strain.csv')
        data=np.array(sdata.values)
        filename=[]
        ########################################Error for Strain and PVLoop        
        pdata = pd.read_csv(path+'Error.csv')
        data_1=np.array(pdata.values)
        filename1=[]
        part = []; err = []
        color=['indianred','maroon','red','sienna','chocolate','goldenrod',
               'yellowgreen','forestgreen','lime','lightseagreen','cyan','deepskyblue',
               'navy','blueviolet','indigo','magenta']
        #######################################Tmax 
        T1data = pd.read_csv(str(pig_)+'echo/'+'Tmax.csv')
        T2data = pd.read_csv(str(pig_)+'mri/'+'Tmax.csv')
        data_1=np.array(T1data.values)
        data_2=np.array(T2data.values)
        part = ['ECHO','MRI']; Tmax = [[],[],[]]
        m=0
        maxT = max(data_2[:,1])
        if  max(data_1[:,1]) > max(data_2[:,1]):
            maxT = max(data_1[:,1])
        filename1.append('Tmax')
        print(max(data_1[:,1]),max(data_2[:,1]))
        plt.figure(figsize=(7,5))
        plt.plot(data_1[:,0]*total_t/29*1000, data_1[:,1]/1000,'-', markersize=5, markeredgewidth=5,label='ECHO' ,color='blue')
        plt.plot(data_1[:,0]*total_t/29*1000, data_2[:,1]/1000,'-', markersize=5, markeredgewidth=5,label ='MRI' ,color='darkorange')
        plt.legend(loc='lower center', bbox_to_anchor=(0.3, 0),  frameon=False, ncol=1, fontsize=24)# borderaxespad= -3,
        plt.ylabel(r'Tmax (kPa)', font1)
        plt.xlabel(r'Time (ms)', font1)
        y_ticks = np.linspace(0, maxT/1000, 3)
        x_ticks = np.linspace(0, total_t*1000, 3)
        plt.yticks(y_ticks)
        plt.xticks(x_ticks)
        plt.yticks(fontsize=24, rotation=0, fontname="Times New Roman")
        plt.xticks(fontsize=24, rotation=0, fontname="Times New Roman")
        plt.tight_layout()
        plt.savefig(path+filename1[0])
        plt.close('all')