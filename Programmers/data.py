proc reg data=Week2.Life_expectancy;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling;
run;
quit;


proc reg data=Week2.Life_expectancy;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling /selection=forward sle=0.1;
run;
quit;


proc reg data=Week2.Life_expectancy;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling /selection=backward sls=0.1;
run;
quit;


proc reg data=Week2.Life_expectancy;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling /selection=stepwise sle=0.1 sls=0.1;
run;
quit;



/*Ridge*/
ods graphics on;
proc reg data=Week2.Life_expectancy outseb outstb outvif outest=Week2.Life_expectancy
ridge=0.1 to 0.2 by .005;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling ;
plot / ridgeplot ;
run;
quit;


proc print data=Week2.Life_expectancy;
var _RIDGE_ Adult_Mortality infant_deaths Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling ;
where _TYPE_ = 'RIDGEVIF';
run;
quit;

title1 'Variance Inflation Factors';
proc gplot data=Week2.Life_expectancy ;
plot (model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling ) * _RIDGE_ / overlay;
where _TYPE_ = 'RIDGEVIF';
run;
quit;

proc reg data=Week2.Life_expectancy outvif outest=Week2.Life_expectancy
ridge=0.145;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling ;
run;
quit;

proc print data=Week2.Life_expectancy;
run;


/*Lasso model*/
proc glmselect data= Week2.Life_expectancy plots(stepaxis=normb)=coefficients;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling / 
selection=lasso(stop=none choose=aic);
run;
quit;


/*Elastic net model*/
proc glmselect data= Week2.Life_expectancy plots=all;
model Life_expectancy=Adult_Mortality infant_deaths	Alcohol	percentage_expenditure HepatitisB Measles BMI under_five_deaths Polio Total_expenditure Diphtheria HIV_AIDS GDP Population	thinness_1_19_years	thinness_5_9_years Income_composition_of_resources Schooling / 
selection=elasticnet(stop=none L1=0.145 L2low=0 L2high=1 choose= aic);
run;
